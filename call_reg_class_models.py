# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:46:41 2017

@author: CWilkens
"""

from Classification_Models import Call_KNN_Classi,Call_Support_Vector_Classi,Call_QDA_Classi
from Regression_Models import Call_DecisionTree_Reg,Call_Bagging_Reg,Call_GradientBoosting_Reg


def call_classification_models(X_train, y_train, X_test, y_test):
    print('')
    print('Classification')
    print('KNN Accuracy Score: ', Call_KNN_Classi(X_train, y_train, X_test, y_test))
    print('SVM Accuracy Score: ', Call_Support_Vector_Classi(X_train, y_train, X_test, y_test))
    print('QDA Accuracy Score: ', Call_QDA_Classi(X_train, y_train, X_test, y_test))
    print('')    


def call_regression_models(X_train_reg, y_train_reg, X_test_reg, y_test_reg):
    print('Regression')
    print ('Decission Tree Regressor R2 Score: ', Call_DecisionTree_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print ('Bagging Regression R2 Score: ',Call_Bagging_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
    print ('Gradient Boosting Regression R2 Score: ',Call_GradientBoosting_Reg(X_train_reg, y_train_reg, X_test_reg, y_test_reg))
     