#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors
    
    Sara has label 0
    Chris has label 1

"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import accuracy_score

## reduce training set size
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

# param_grid = {'C': [1, 10, 100, 1000, 10000],
              # 'kernel': ['linear', 'rbf'], }

clf = SVC(kernel='rbf', C=10000)
# clf = GridSearchCV(SVC(), param_grid)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print "Accuracy score: ", accuracy_score(pred, labels_test)
# print "Best estimator: ", clf.best_estimator_
# print "Predictions 10, 26, 50: ", pred[10], pred[26], pred[50]
print "Number of predicted emails by Chris (1): ", sum(pred == 1)

#########################################################


