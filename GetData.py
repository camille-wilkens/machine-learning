# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:46:41 2017

@author: CWilkens
"""

import pandas as pd
import os
import numpy as np



def get_classification_Data(email_file_directory,email_file_name): 
    """

    """
    fn=os.path.join(email_file_directory, "{}.csv".format(str(email_file_name)))
    df = pd.read_csv(fn, index_col=["Date","POI"],parse_dates=["Date"], header=0,usecols=["file", "Date","POI","Percentage_Bad_Words_count","Percentage_Lit_Words_count","Total_Words_count","Bad_Words_count","Lit_Words_count"])
    df = df[np.isfinite(df['Percentage_Bad_Words_count'])]
    
    return df
def get_regression_Data(email_file_directory,email_file_name): 
    """

    """
    fn=os.path.join(email_file_directory, "{}.csv".format(str(email_file_name)))
    df = pd.read_csv(fn, index_col=["Date","POI"],parse_dates=["Date"], header=0,usecols=["file", "Date","POI","Percentage_Bad_Words_count","Percentage_Lit_Words_count","Total_Words_count","Bad_Words_count","Lit_Words_count"])
    df = df[np.isfinite(df['Percentage_Bad_Words_count'])]

    return df
