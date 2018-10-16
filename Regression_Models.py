# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 07:55:59 2017

@author: CWilkens
"""
"""
Step 9:
Call Regression Models - Decision Tree Regressor, Bagging Regression & Gradient Boosting Regression
Use Default paramaters (except for Decision Tree using GridSearch) and return R2 score for each model

Call Plot Regression Model Prediction Scores for all Models
Call Plot Learning Curve and Model Complexity for Decision Tree

"""

from sklearn import  ensemble
from sklearn.metrics import r2_score,make_scorer
from Regression_Plot import plot_model_complexity
from Regression_Plot import plot_model_learning
from Regression_Plot import plot_regression_predictions
from sklearn.grid_search import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.cross_validation import ShuffleSplit

def Call_DecisionTree_Reg(X_train, y_train, X_test, y_test):
    # Create regressor = Decision Tree Regressor
    regressor = DecisionTreeRegressor()

    # Set parameters max depth
#    parameters = [{'max_depth':(1,2,3,4,5,6,7,8,9,10),'presort':['True']}]
    parameters = [{'max_depth':(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20),'presort':['True']}]

 #   cv_sets = ShuffleSplit(X_train.shape[0], n_iter = 10, test_size = 0.20, random_state = 0)
    # define R2 Scorer
    scorer = None
#    scorer = make_scorer(r2_score, greater_is_better=True)
    scorer = make_scorer(r2_score)
    # GridSearchCV object
    new_regressor = None
    new_regressor = GridSearchCV(regressor, parameters,scoring=scorer)
#    new_regressor = GridSearchCV(regressor, parameters)
    print ('print regressor: ', new_regressor)
    # Using GridSearch, fit to data to find best parameters
    
    new_regressor.fit(X_train, y_train)
    prediction = new_regressor.predict(X_test)
#    regressor.fit(X_train, y_train)
#    prediction = regressor.predict(X_test)
    print("Decision Tree Regressor Score: ",new_regressor.score(X_test, y_test) )
    print("Regressor Parameters  ",new_regressor)
    R2 = r2_score(y_test, prediction)
    
    # plot Prediction
    plot_regression_predictions(y_test, 'Decision Tree Regressor',prediction)
    # Plot Model Learning
    plot_model_learning(X_train,y_train)
    # Plot Model Complexity
    plot_model_complexity(X_train,y_train)


    return R2

    
def Call_Bagging_Reg(X_train, y_train, X_test, y_test):

    clf = ensemble.BaggingRegressor()  
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    print("Bagging Regressor Score: ",clf.score(X_test, y_test) )

    R2 =r2_score(y_test, prediction)
    
     # plot Prediction
    plot_regression_predictions(y_test, 'Bagging Regressor',prediction)
    
    return R2  



def Call_GradientBoosting_Reg(X_train, y_train, X_test, y_test):
    
    clf = ensemble.GradientBoostingRegressor()
    clf.fit(X_train, y_train)
    prediction = clf.predict(X_test)
    print("Gradient Boosting Regressor Score: ",clf.score(X_test, y_test) )
    R2 =r2_score(y_test, prediction)
    
     # plot Prediction
    plot_regression_predictions(y_test, 'Gradient Boosting Regressor',prediction)
    
    return R2
    
