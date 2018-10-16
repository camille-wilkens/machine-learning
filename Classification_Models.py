# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 07:55:59 2017

@author: CWilkens
"""
from sklearn.qda import QDA
from sklearn.svm import SVC
from sklearn import neighbors


        
def Call_KNN_Classi(X_train, y_train, X_test, y_test):

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)

    return accuracy

def Call_Support_Vector_Classi(X_train, y_train, X_test, y_test):
    

    clf = SVC(kernel="linear",C=100.0)

    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    print ('SVC Parameters: ', clf)
    return accuracy
    

def Call_QDA_Classi(X_train, y_train, X_test, y_test):

    clf = QDA()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return accuracy

