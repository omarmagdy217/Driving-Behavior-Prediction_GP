import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC
######################################
# file to read data from
Data = pd.read_csv(" ")
X = Data.drop('Class', axis=1)
Y = Data['Class']
# to make cross validation, 20% of data are test examples
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, shuffle=True)

######################################
# train the model
svclassifier = SVC(kernel='poly', degree=5)
svclassifier.fit(X_train, y_train)

######################################
# to predict for new inputs
y_pred = svclassifier.predict(X_test)

######################################

# print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
# precision: for all instances classified positive, what percent was correct?
# recall: for all instances that were actually positive, what percent was classified correctly?
# f1-score: weighted harmonic mean of precision and recall such that the best score is 1.0 and the worst is 0.0 (2*prod/sum)
# support: number of actual occurrences of the class in the specified data set
