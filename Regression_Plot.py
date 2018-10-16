# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 07:55:59 2017

@author: CWilkens
"""
"""
Step 9:
Plot Regression Model Prediction Scores


"""
from sklearn.tree import DecisionTreeRegressor
import numpy as np

from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import sklearn.learning_curve as curves
from sklearn.cross_validation import ShuffleSplit

from pandas import DatetimeIndex as dt
import pandas as pd

def plot_regression_predictions(y_test, model_name,prediction):
    y_test1 = y_test.copy()
    y_test1 = y_test1.reset_index()
    
 #   y_test1['Date'] = dt.strftime(y_test.index.get_level_values('Date'), "%Y-%m-%d")
    y_test1['Date'] = dt.strftime(y_test.index.get_level_values('Date'), "%Y-%m")
    y_test1['Date'] = pd.to_datetime(y_test1['Date'])
    y_test1.drop('POI',axis=1,inplace=True)

    f, ax = plt.subplots(figsize=(8,5))
    ax.plot(y_test1.Date,y_test1.Percentage_Bad_Words_count,label='% of Total Email Messages')
    ax.plot(y_test1.Date,prediction,color='red',label="% of Financial Negative Words Predicted")
    ax.plot_date(y_test1.Date,prediction,color='black')
    ax.set_title(model_name +': % of Financial Negative Words Predicted by Date')   
    ax.set_xlabel("Date",rotation=0)
    plt.xticks(rotation = 90)
    ax.set_ylabel("% Of Negative Word")
    ax.legend(loc="upper right")
    f.autofmt_xdate()
    plt.show()
    
def plot_model_learning(X, y):
    """ Calculates the performance of several models with varying sizes of training data.
        The learning and testing scores for each model are then plotted. 
        Code from Udacity's Machine Learning Nanodegree Boston Housing Project"""
    
    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(X.shape[0], n_iter = 10, test_size = 0.2, random_state = 0)

    # Generate the training set sizes increasing by 50
    train_sizes = np.rint(np.linspace(1, X.shape[0]*0.8 - 1, 9)).astype(int)

    # Create the figure window
    fig = plt.figure(figsize=(10,7))

    # Create three different models based on max_depth
    for k, depth in enumerate([1,3,5,10]):
        
        # Create a Decision tree regressor at max_depth = depth
        regressor = DecisionTreeRegressor(max_depth = depth)

        # Calculate the training and testing scores
        sizes, train_scores, test_scores = curves.learning_curve(regressor, X, y, \
            cv = cv, train_sizes = train_sizes, scoring = 'r2')
        
        # Find the mean and standard deviation for smoothing
        train_std = np.std(train_scores, axis = 1)
        train_mean = np.mean(train_scores, axis = 1)
        test_std = np.std(test_scores, axis = 1)
        test_mean = np.mean(test_scores, axis = 1)

        # Subplot the learning curve 
        ax = fig.add_subplot(2, 2, k+1)
        ax.plot(sizes, train_mean, 'o-', color = 'r', label = 'Training Score')
        ax.plot(sizes, test_mean, 'o-', color = 'g', label = 'Testing Score')
        ax.fill_between(sizes, train_mean - train_std, \
            train_mean + train_std, alpha = 0.15, color = 'r')
        ax.fill_between(sizes, test_mean - test_std, \
            test_mean + test_std, alpha = 0.15, color = 'g')
        
        # Labels
        ax.set_title('max_depth = %s'%(depth))
        ax.set_xlabel('Number of Training Points')
        ax.set_ylabel('Score')
        ax.set_xlim([0, X.shape[0]*0.8])
        ax.set_ylim([-0.05, 1.05])
    
    # Visual aesthetics
    ax.legend(bbox_to_anchor=(1.05, 2.05), loc='lower left', borderaxespad = 0.)
    fig.suptitle('Decision Tree Regressor Learning Performances', fontsize = 16, y = 1.03)
    fig.tight_layout()
    fig.show()

    
def plot_model_complexity(X,y):
    """ Calculates the model complexity of several models with varying sizes of training data.
    The learning and testing scores for each model are then plotted
    Code from Udacity's Machine Learning Nanodegree Boston Housing Project"""
    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(X.shape[0], n_iter = 10, test_size = 0.2, random_state = 0)
    
    # Vary the max_depth parameter from 1 to 10
    max_depth = np.arange(1,11)
    
    # Calculate the training and testing scores
    train_scores, test_scores = curves.validation_curve(DecisionTreeRegressor(), X, y, \
#    param_name = "max_depth", param_range = max_depth, cv = cv, scoring = 'r2')
    param_name = "max_depth", param_range = max_depth, cv = cv, scoring = 'r2')
  
    # Find the mean and standard deviation for smoothing
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    # Plot the validation curve
    plt.figure(figsize=(7, 5))
    plt.title('Decision Tree Regressor Complexity Performance')
    plt.plot(max_depth, train_mean, 'o-', color = 'r', label = 'Training Score')
    plt.plot(max_depth, test_mean, 'o-', color = 'g', label = 'Validation Score')
    plt.fill_between(max_depth, train_mean - train_std, \
    train_mean + train_std, alpha = 0.15, color = 'r')
    plt.fill_between(max_depth, test_mean - test_std, \
    test_mean + test_std, alpha = 0.15, color = 'g')
    
    # Visual aesthetics
    plt.legend(loc = 'lower right')
    plt.xlabel('Maximum Depth')
    plt.ylabel('Score')
    plt.ylim([-0.05,1.05])
    plt.show()
    
def metric(y_true, y_predict):
    """ Calculates and returns the total error between true and predicted values
        based on a R2 """

    score =  r2_score(y_true, y_predict) 
   
    # Return the score
    return score