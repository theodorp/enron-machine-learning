#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.metrics import accuracy_score

# ## KNN
# from sklearn.neighbors import KNeighborsClassifier

# clf = KNeighborsClassifier()
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)

# print "Accuracy score: ", accuracy_score(labels_test, pred) 

# ## Adaboost
# from sklearn.ensemble import AdaBoostClassifier

# clf = AdaBoostClassifier()
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)

# print "Accuracy score: ", accuracy_score(labels_test, pred) 

# ## Random Forest
# from sklearn.ensemble import RandomForestClassifier

# clf = RandomForestClassifier()
# clf.fit(features_train, labels_train)
# pred = clf.predict(features_test)

# print "Accuracy score: ", accuracy_score(labels_test, pred) 

## Non-Linear SVM
from sklearn import svm
clf = svm.NuSVC(gamma=45)
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

print "Accuracy score: ", accuracy_score(labels_test, pred) 


print features_train

# try:
prettyPicture(clf, features_test, labels_test, show=True)
# except NameError:
    # pass
