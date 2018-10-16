# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:54:25 2017

@author: CWilkens
"""

"""
Data Preprocessing - Step 2:  Extract relevant email objects from the messages field.  Message_Body, To, From & Date fields 
were extracted from the original messages field and all words were made lower case which is 
required for the word matching of the POI email addresses and financial negative & litigation words.   
The POI email address list will be compared to the email address of the sender – “From” for each email message. Create new field called POI,  If these email addresses match, this email message will be marked as a “POI” email message.

Created new Features for future use, these features will be updated during keyword matching:
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
import numpy as np  # arrays and numerical processing
import email

def add_columns(email_file_directory):
    pd.options.mode.chained_assignment = None  # default='warn'
    
    email_filename = "emails_clean.csv" 
    
    t1 = time()

    emails = pd.read_csv(email_file_directory+'inputs/'+email_filename)       
    poi_email_address = pd.read_csv(email_file_directory+'inputs/'+'poi_email_list.csv', header=None)
    poi_email_address.columns = ["poi_email"]
    
    
    # Parse the emails into a list email objects
    msg_body = get_messages(emails)
    
    
    emails["Message_Body"] = msg_body
    
    messages = list(map(email.message_from_string, emails['message']))
    emails.drop('message', axis=1, inplace=True)
    
    
    # Get fields from parsed email objects
    keys = messages[0].keys()
    for key in keys:
        emails[key] = [doc[key] for doc in messages]
    
    
    emails["Message_Body"] = msg_body
    
    """ Remove Extra Columns that are not required  """
    
    emails.drop('Mime-Version', axis=1, inplace=True)

    emails.drop('Content-Type', axis=1, inplace=True)
    emails.drop('Content-Transfer-Encoding', axis=1, inplace=True)
    emails.drop('X-FileName', axis=1, inplace=True)
    
    
    # Extract the root of file as Inbox Owner
    emails['Inbox_Owner'] = emails['file'].map(lambda x:x.split('/')[0])
    
    # Identify the POI - if matchining email from POI Email Address exists
    emails['POI'] = emails['From'].isin(poi_email_address['poi_email'])

    del messages
    emails.head()
    
    
    
    emails['Date'] = pd.to_datetime(emails['Date'], infer_datetime_format=True)
    emails.dtypes
    
    
    """
    Add additional required fields for future use
    """
    emails["Bad_Words"] =np.nan
    emails["Bad_Words_count"] = np.nan
    emails["Total_Words_count"]= np.nan
    emails["Percentage_Bad_Words_count"]= np.nan
    emails["Lit_Words"] =np.nan
    emails["Lit_Words_count"] = np.nan
    emails["Percentage_Lit_Words_count"]= np.nan

# include only the years 1999 - 2002 (remove 1219 rows of outlier data)
    emails = emails[emails['Date'].dt.year.isin([1999,2000,2001,2002])]
    emails.to_csv(email_file_directory+'outputs/'+'cleansed_emails_Parsed.csv',index=False)
    
    t2 = time()
    print(t1,t2,"Time Taken in mins :",t2-t1)

def get_messages(df):
    messages = []
    for item in df["message"]:
        # Return a message object structure from a string
        e = email.message_from_string(item)    
        # get message body  
        message_body = e.get_payload()
        message_body = message_body.lower()
        messages.append(message_body)
                       
    return messages
    
 
if __name__ == "__main__":
    add_columns()     
 
     
