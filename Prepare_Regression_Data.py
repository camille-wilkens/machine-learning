# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 07:53:46 2017

@author: CWilkens
"""


def regression_data_prep(email_data_frame_reg):
    """
    POI are treated as training set and non -POI are testing sets.
    Input/features is total number of words
    output/measurable
    """
    email_data_frame_reg=email_data_frame_reg.reindex(columns=['file','Percentage_Bad_Words_count','Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count'])

    
    train = email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==True]
    test = email_data_frame_reg[email_data_frame_reg.index.get_level_values('POI')==False]    


    
    features = email_data_frame_reg.columns[2:]
    print ('Features for Regression Models:',features)
    """
    Set the values for X_train , y_train, X_test, y_test
    """
    X_train =train[features]

    y_train =train['Percentage_Bad_Words_count']
    X_test = test[features]
   # y_test =test[['Bad_Words_count','Lit_Words_count']]
    y_test =test['Percentage_Bad_Words_count']
    
    return X_train, y_train, X_test, y_test
