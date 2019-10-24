# Import statements
import pandas as pd
import numpy as np
###########################################
# Import 'accuracy_score'
from sklearn.metrics import accuracy_score

def performance_metric(y_true, y_predict):
    """ Calculates and returns the performance score between 
        true and predicted values based on the metric chosen. """
    
    # Calculate the performance score between 'y_true' and 'y_predict'
    score = accuracy_score(y_true, y_predict)
    
    # Return the score
    return score
###########################################
# Import 'make_scorer', 'LDA', and 'GridSearchCV'
from sklearn.metrics import make_scorer
from sklearn.lda import LDA
from sklearn.model_selection import GridSearchCV

def fit_model(X, y):
    """ Performs grid search over the 'max_depth' parameter for a 
        decision tree regressor trained on the input data [X, y]. """
    
    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(n_splits = 10, test_size = 0.20, random_state = 0)

    # Create a linear discriminant analysis object
    clf = LDA()

    # Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
    params = {'solver':['svd', 'lsqr', 'eigen'], 'tol':[0.0001, 0.001, 0.01]}

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
###########################################
# Import 'train_test_split'
from sklearn.model_selection import train_test_split

# Read the data.
data = np.asarray(pd.read_csv('data.csv', header=None))
# Assign the features to the variable X, and the labels to the variable y. 
Bands = data[:,0:5]
state = data[:,-1]

# Shuffle and split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(Bands, state, test_size=0.2, random_state=42)

# Success
print("Training and testing split was successful.")
###########################################
# Fit the training data to the model using grid search
model = fit_model(X_train, y_train)

# Produce the value for 'solver'
print("Parameter 'solver' is {} for the optimal model.".format(model.get_params()['solver']))

# Make predictions. Store them in the variable y_pred.
y_pred = model.predict(X_test)
  
# Show predictions
for i, state in enumerate(y_pred):
    print("Predicted mental state for test {}'s bands: ${:,.2f}".format(i+1, state))
###########################################
# Import 'f1_score'
from sklearn.metrics import f1_score

# Calculate the f1 score and assign it to the variable score.
score = f1_score(y_test, y_pred)

# Print score
print("F1 score:", score) 
