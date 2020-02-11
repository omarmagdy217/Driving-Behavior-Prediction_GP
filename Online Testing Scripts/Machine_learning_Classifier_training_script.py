import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import visuals as vs
from sklearn.metrics import accuracy_score
from sklearn.metrics import make_scorer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from IPython.display import display
from time import time
from sklearn.metrics import f1_score
import pickle


def delete_empty_rows(file_path, new_file_path):
    data = pd.read_csv(file_path, skip_blank_lines=True)
    data.dropna(how="all", inplace=True)
    data.to_csv(new_file_path, header=True)

def performance_metric(y_true, y_predict):
    """
        Calculates and returns the performance score between
        true and predicted values based on the metric chosen.
    """
    # Calculate the performance score between 'y_true' and 'y_predict'
    score = accuracy_score(y_true, y_predict)
    # Return the score
    return score


def fit_model(X, y):
    """
        Performs grid search over the 'max_depth' parameter for a
        decision tree regressor trained on the input data [X, y].
    """
    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(n_splits=10, test_size=0.20, random_state=0)
    # Create a linear discriminant analysis object
    clf = SVC(kernel='rbf', class_weight='balanced')
    # Create a dictionary for the parameters
    params = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}
    # Transform 'performance_metric' into a scoring function using 'make_scorer'
    scoring_fnc = make_scorer(performance_metric)
    # Create the grid search cv object --> GridSearchCV()
    # Make sure to include the right parameters in the object:
    # (estimator, param_grid, scoring, cv) which have values 'clf', 'params', 'scoring_fnc', and 'cv_sets' respectively.
    grid = GridSearchCV(clf, params, scoring=scoring_fnc, cv=cv_sets)
    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)
    # Return the optimal model after fitting the data
    return grid.best_estimator_


def pca_projection(good_data, n_components):
    # Apply PCA by fitting the good data with only two dimensions
    pca = PCA(n_components=n_components).fit(good_data)
    # Transform the good data using the PCA fit above
    reduced_data = pca.transform(good_data)
    # Create a DataFrame for the reduced data
    columns = ['Dimension 1', 'Dimension 2', 'Dimension 3']
    return pd.DataFrame(reduced_data, columns=columns[:n_components]), pca




def main():
    # Read the data.
    delete_empty_rows('data_set_file_omar.csv', 'data_set_ML.csv')
    raw_data = pd.read_csv('data_set_ML.csv')
    # Split the data into features and target label
    target_raw = raw_data[raw_data.columns[-1]]
    features_raw = raw_data.drop(raw_data.columns[-1], axis=1)
    # Print data shape.
    print("The shape of the data: {}".format(raw_data.shape))
    features_log_transformed = features_raw.apply(lambda x: np.log(x + 1))

    # Calculate Q1 (25th quantile of the data) for all features.
    Q1 = features_log_transformed.quantile(0.25)
    # Calculate Q3 (75th quantile of the data) for all features.
    Q3 = features_log_transformed.quantile(0.75)
    # Use the interquartile range to calculate an outlier step (1.5 times the interquartile range).
    IQR = Q3 - Q1
    step = 1.5 * IQR
    # Remove the outliers from the dataset.
    features_log_transformed_out = features_log_transformed[
        ~((features_log_transformed < (Q1 - step)) | (features_log_transformed > (Q3 + step))).any(axis=1)]
    # Join the features and the target after removing outliers.
    preprocessed_data_out = features_log_transformed_out.join(target_raw)
    target_raw_out = preprocessed_data_out[preprocessed_data_out.columns[-1]]
    # Print data shape after removing outliers.
    print("The shape of the data after removing outliers: {}".format(preprocessed_data_out.shape))

    # Initialize a scaler, then apply it to the features
    scaler = MinMaxScaler()  # default=(0, 1)
    features_log_minmax_transform_out = pd.DataFrame(scaler.fit_transform(features_log_transformed_out),columns=features_raw.columns)
    # Show an example of a record with scaling applied
    display(features_log_minmax_transform_out.head())

    # Assign preprocessed data frame to 'good_data'.
    good_data = features_log_minmax_transform_out
    # Assign the features to the variable Bands, and the labels to the variable state.
    Bands = np.array(good_data)
    state = np.array(target_raw_out)
    # Shuffle and split the data into training and testing subsets.
    X_train, X_test, y_train, y_test = train_test_split(Bands, state, test_size=0.2, random_state=42, shuffle=True)
    # Success
    print("Training and testing split was successful.")

    # Project data on two dimensions
    reduced_data, pca = pca_projection(good_data, 2)

    # Fitting the PCA algorithm with our training data.
    pca = PCA().fit(X_train)

    # Plotting the Cumulative Summation of the Explained Variance.
    plt.figure(figsize=(14, 7))
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.ylabel('Variance (%)')  # For each component.
    plt.title('Pulsar Dataset Explained Variance')
    #plt.show()

    # From the Explained Variance graph.
    n_components = 20

    print("Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))
    t0 = time()
    # Create an instance of PCA, initializing with n_components=n_components and whiten=True
    pca = PCA(n_components=n_components)
    # Pass the training dataset (X_train) to pca's 'fit()' method
    pca = pca.fit(X_train)
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print("Explained variance ratios:", pca.explained_variance_ratio_ * 100)
    print("done in %0.3fs" % (time() - t0))

    # Fit the training data to the model using grid search
    model = fit_model(X_train_pca, y_train)
    # Produce the value for 'gamma' and 'C'
    print("Parameter 'gamma' is {} for the optimal model.".format(model.get_params()['gamma']))
    print("Parameter 'C' is {} for the optimal model.".format(model.get_params()['C']))

    # Make predictions. Store them in the variable y_pred.
    y_pred = model.predict(X_test_pca)
    # Label states class.
    states_class = ['Focused', 'De-Focused', 'Drowsy']
    # Show predictions
    for i, state in enumerate(y_pred):
        print("Predicted mental state for test {}'s bands: {}".format(i + 1, states_class[int(state - 1)]))

    # Calculate the f1 score and assign it to the variable score.
    score = f1_score(y_test, y_pred, average='micro')
    # Print score.
    print("F1 score: %0.1f %%" % (score * 100))

    # save the model to disk
    filename = 'finalized_model.sav'
    pickle.dump(model, open(filename, 'wb'))
    #save PCA
    pickle.dump(pca, open("pca.pkl", "wb"))



    # some time later...
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    print(X_test_pca.shape)
    y_pred = loaded_model.predict(X_test_pca)
    # Label states class.
    states_class = ['Focused', 'De-Focused', 'Drowsy']
    # Calculate the f1 score and assign it to the variable score.
    score = f1_score(y_test, y_pred, average='micro')
    print("F1 score: %0.1f %%" % (score * 100))

if __name__ == "__main__":
    main()

