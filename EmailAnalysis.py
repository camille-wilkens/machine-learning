# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 07:55:59 2017

@author: CWilkens

"""
import numpy as np
from cleanCSVMailFile import getCleanEmail
from time import time
import pandas as pd
import os
from pandas import DatetimeIndex as dt
from parse_csv_file_to_mail_columns import add_columns
from Calculate_Negative_Words import CalcuateNegativeWords
from GetData import get_classification_Data,get_regression_Data
from Prepare_Classification_Data import classification_data_prep
from Prepare_Regression_Data import regression_data_prep
from call_reg_class_models import call_classification_models, call_regression_models
from dat_exploratory_plot import plot_exploration

t1 = time()


"""
Change Project Directory 
"""
project_directory = 'C:/Training/Udacity/machine-learning/capstone/email-analysis/'
email_file_name ='email_csv_with_bad_words'

"""
Step1:
Data Preprocessing: 
 Remove special characters from original email CSV file 
"""
getCleanEmail(project_directory)
"""
Step 2: 
Data Preprocessing: 
   Parse the cleaned emails into relevant email objects..  
"""
add_columns(project_directory)

"""
Step 3:
Data Preprocessing: 
   Compare & count words in message body to Loughran and McDonald’s financial sentiment dictionary -
LoughranMcDonald_Negative & LoughranMcDonald_Litigious files
"""
CalcuateNegativeWords(project_directory)



"""
Step 4: 
Get Data for Classifcation training & test datasets:
Create New Dataframe with Indexed Columns ["Date","POI"] and select only required columns 
needed for modeling - ['file','Percentage_Bad_Words_count','Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count']
"""
email_data_frame_class = get_classification_Data(project_directory+'outputs/',email_file_name)

"""
Step 5: 
Prepare Classifcation training & test datasets:
 transform the number of negative words within an email message into a label called Classifcation1
 with two types of classification - “YES_Negative” (Email Message contains Financial Negative 
 words) and “NO_negative” (Email Message does not contain financial negative words)
The inputs/features I will be using in the Classification Models:
Total_Words_count - Total words found in email message 
Bad_Words_count - # of Financial Negative words found in email message
Lit_Words_count  - # of Financial Litigation words found in email message
Percentage_Lit_Words_count - # of Financial Litigation words (Lit_Words_count) found in email message/Total Word Count Found in email message 

The output/target variable will be “Classification1” 
 
"""
X_train, y_train, X_test, y_test = classification_data_prep(email_data_frame_class)

print('')
print('Classification DataSet:')
print("Shape X_train:",X_train.shape)
print("Shape y_train:",y_train.shape)
print("Shape X_test:",X_test.shape)
print("Shape y_test:",y_test.shape)
print('')


"""
Step 6: 
Get Data for Regression training & test datasets:
a) Create New Dataframe with Indexed Columns ["Date","POI"] and select only required columns 
needed for modeling - ['file','Percentage_Bad_Words_count','Bad_Words_count', 'Total_Words_count','Lit_Words_count','Percentage_Lit_Words_count']
"""
email_data_frame_reg = get_regression_Data(project_directory+'outputs/',email_file_name)

"""
Step 7: 
Prepare Regression training & test datasets:
transform the number of occurrences of financial negative words into a numerical number called “Percentage of Negative Words” which is the number of financial negative words in an email message divided by total number of words in the email message. 
The inputs/features I will be using in the Regression Models:
Total_Words_count - Total words found in email message 
Bad_Words_count - # of Financial Negative words found in email message
Lit_Words_count  - # of Financial Litigation words found in email message
Percentage_Lit_Words_count - # of Financial Litigation words (Lit_Words_count) found in email message/Total Word Count Found in email message 

The target variable will be Percentage of Negative Words
"""
X_train_reg, y_train_reg, X_test_reg, y_test_reg  = regression_data_prep(email_data_frame_reg)
t2 = time()


print('')
print('Regression DataSet:')
print("Shape X_train:",X_train_reg.shape)
print("Shape y_train:",y_train_reg.shape)
print("Shape X_test:",X_test_reg.shape)
print("Shape y_test:",y_test_reg.shape)
print('')


"""
Step 8:
Call Classification Models - SVC,KNN,QDA
Use Default paramaters and return accurary score

"""

call_classification_models(X_train, y_train, X_test, y_test)

t3 = time()
#print(' Time taken for All Classification = ', (t3-t2)/60 )

"""
Step 9:
Call Regression Models - Decision Tree Regressor, Bagging Regression & Gradient Boosting Regression
Use Default paramaters (except for Decision Tree using GridSearch) and return R2 score for each model

Plot Regression Model Prediction Scores
Plot Learning Curve and Model Complexity for Decision Tree

"""
call_regression_models(X_train_reg, y_train_reg, X_test_reg, y_test_reg)

t4 = time()
print(' Time taken for All Regression = ', (t4-t3)/60 )


"""
Step 10:
Plot Exploratory Visualizations
 - Summary of Messages by Year
 - Summary of Message by Year & Month
 - Summary of Financial Negative Words by Year & Month
"""

plot_exploration(email_data_frame_class)


print(' Total Time taken = ', (t4-t1)/60 )


    

    
    
