# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 07:53:46 2017

@author: CWilkens
"""

"""
Data Preprocessing - Step 3: Perform keyword matching with the Financial Sentiment Dictionary -
LoughranMcDonald_Negative & LoughranMcDonald_Litigious filesv (included in the scope of this project).  
Updated the following fields with the Financial Negative and Financials Words found in each email message:
Total_Words_count - Total words found in email message 
Bad_Words –  The Financial Negative word(s) found in the email message
Bad_Words_count - # of Financial Negative words found in email message
Percentage_Bad_Words_count  - % of Bad Words Found in email message (# of  Financial Negative words found in email message/Total Words Found in email message)
Lit_Words – The financial litigation word(s) found in email message
Lit_Words_count  - # of Financial Litigation words found in email message
Percentage_Lit_Words_count - # of Financial Litigation words (Lit_Words_count) found in email message/Total Word Count Found in email message 
"""
from time import time
import pandas as pd  # DataFrame structure and operations
#import numpy as np  # arrays and numerical processing
#import email


def CalcuateNegativeWords(project_directory):
    pd.options.mode.chained_assignment = None  # default='warn'
    
    email_filename = "cleansed_emails_Parsed.csv"
    FinNeg_filename = "LoughranMcDonald_Negative.csv"
    FinLit_filename = "LoughranMcDonald_Litigious.csv"
   
    t1 = time()


    emails = pd.read_csv(project_directory+'outputs/' +email_filename)      

    FinNeg = pd.read_csv(project_directory+'inputs/' +FinNeg_filename, header=None)
    FinNeg.columns = ["word","year"]
    FinNeg.drop('year', axis=1, inplace=True)
    FinNeg["word"] = FinNeg["word"].str.lower()
        
    
    FinLit = pd.read_csv(project_directory+'inputs/' +FinLit_filename, header=None)
    FinLit.columns = ["word","year"]

    #print(FinLit.columns)
    FinLit.drop('year', axis=1, inplace=True)
    #print(FinLit.columns)
    FinLit["word"] = FinLit["word"].str.lower()
    
    error_frame = pd.DataFrame({'Line_Number':[' error at row :1000000000']})
    #print(error_frame)
    
    
    Test_Bad_Words =[]
    Result_Bad_Words =''
    Result_bad_word_count = 0
    
    Test_Lit_Words =[]
    Result_Lit_Words =''
    Result_lit_word_count = 0
    
    error_frame.to_csv(project_directory+'outputs/' +'error_email_csv_with_bad_words.csv',index=False)
    
    #error_frame_words=[]
    
    for msg_count in range(0,len(emails["file"])):
        try:
            k = emails['Message_Body'][msg_count].split()
            Test_Bad_Words=(FinNeg[FinNeg['word'].isin(k)])
            Test_Lit_Words=(FinLit[FinLit['word'].isin(k)])
            
            if len(Test_Bad_Words) >0 :
                Result_bad_word_count = len(Test_Bad_Words.values)
                Result_Bad_Words = Test_Bad_Words.values.ravel()
                Result_Bad_Words= ','.join(map(str,Result_Bad_Words))
        #        print(Result_bad_word_count,'---BAD---',Result_Bad_Words)
                
            if len(Test_Lit_Words) >0 :
                Result_lit_word_count = len(Test_Lit_Words.values)
                Result_Lit_Words = Test_Lit_Words.values.ravel()
                Result_Lit_Words= ','.join(map(str,Result_Lit_Words))
        #        print(Result_lit_word_count,'---LITI---',Result_Lit_Words)
                
                
        #    print('--------',msg_count,'-----------') 
            emails['Bad_Words'][msg_count] =Result_Bad_Words
            emails['Bad_Words_count'][msg_count] = Result_bad_word_count
            emails['Total_Words_count'][msg_count] = len(k)
            emails['Percentage_Bad_Words_count'][msg_count] = ((emails['Bad_Words_count'][msg_count])/(emails['Total_Words_count'][msg_count]))
            emails['Lit_Words'][msg_count] = Result_Lit_Words
            emails['Lit_Words_count'][msg_count] = Result_lit_word_count
            emails['Percentage_Lit_Words_count'][msg_count] = ((emails['Lit_Words_count'][msg_count])/(emails['Total_Words_count'][msg_count]))
               
        
            Test_Bad_Words=[]
            Result_Bad_Words =''
            Result_bad_word_count = 0
            
            Test_Lit_Words =[]
            Result_Lit_Words =''
            Result_lit_word_count = 0
        except:

            error_frame['Line_Number']="error at row :"+str(msg_count)
            error_frame.to_csv(project_directory+'outputs/'+'error_email_csv_with_bad_words.csv',mode='a', header=False,index=False)
    #        print("error at row :",msg_count , error_frame_words )
    #        error_frame_words=[]
    emails.to_csv(project_directory+'outputs/' +'email_csv_with_bad_words.csv',index=False)
    # Count words in Subjects and content

    print('shape of the dataframe:', emails.shape)
    # Find number of unique values in each columns
    for col in emails.columns:
        print(col, emails[col].nunique())
        
    emails['number_of_emails'] = emails['Message-ID']    
    emails['negative_wc'] = emails['Bad_Words_count']
    emails['total_wc'] =emails['Total_Words_count']
    
    
    grouped_by_people = emails.groupby('Inbox_Owner').agg({
            'number_of_emails': 'count', 
            'negative_wc': 'sum',
            'total_wc': 'sum',
        })
    grouped_by_people.rename(columns={'number_of_emails': 'N emails', 
                                      'negative_wc': 'Negative word count', 
                                      'total_wc': 'Total word count'}, inplace=True)
    print grouped_by_people.sort('N emails', ascending=False).head()
    
    t2 = time()
    print(t1,t2,"Time Taken in mins :",t2-t1)