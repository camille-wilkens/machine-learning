# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:54:25 2017

@author: CWilkens
"""

"""


Data Preprocessing - Step 1: Removed special characters from the original message field.  
These special characters were identified and replaced with ‘ ‘.    For example, any occurrence 
of  “- -“  was replaced with “ “.   During Step 1, the column message was also restricted to 3,000
characters per message.  New csv file called emails_clean.csv is created in the inputs directory with the cleansed data.

Total rows: 517401

"""

import pandas as pd  


email_filename = "emails.csv"

def getCleanEmail(project_directory): 

    emails = pd.read_csv(project_directory+'inputs/'+email_filename,header=0,delimiter=",",dtype=(str,3000)) 
    emails.message=emails.message.str.replace("--", '')
    emails.message=emails.message.str.replace(r"[\"\',]", '')
    emails.to_csv(project_directory+'inputs/'+'emails_clean.csv',  index=False)
