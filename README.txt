Required Software & packages:
•	Python 2.7.12 |Anaconda 4.0.0 (64-bit)
•	scikit-learn version  0.17.1
•	Pandas version 0.18.0
•	NumPy version 1.10.4
•	 SciPy version 0.17.0
•	pandas_datareader version 0.3.0.post
•	quandl api_version = '2015-04-09'


Project Directory Folders:
/Inputs  - Input Data is stored under Project Directory/Inputs directory 
	(3 files will exist initially in this folder - LoughranMcDonald_Litigious.csv, LoughranMcDonald_Negative.csv, poi_email_list.csv)

/Outputs -  This is where the error file, cleansed email and parsed email with negative words will be stored during execution of EmailAnalysis.py


Source code is stored under the main project folder.


Steps to Run:

1)	Extract machine_learning_capstone_project_cwilkens.zip

2)	In the Main Project Folder: 
	Update the project_directory variable in EmailAnalysis.py 

	Example: 
 	project_directory = 'C:/Training/Udacity/machine-learning/email-analysis/'

3)	Download Enron Email Corpus from Kaggle
	Download Location: https://www.kaggle.com/wcukierski/enron-email-dataset
	Download file is called email.csv
	Download and store emails.csv in the project_directory/inputs folder

4)	Execute EmailAnalysis.py which will call the other supplemental python programs
 	(Run Time on Laptop: 80 minutes)
	
Supplemental Python Programs:
o	cleanCSVMailFile.getCleanEmail
o	parse_csv_file_to_mail_columns.add_columns
o	Calculate_Negative_Words.CalcuateNegativeWords
o	GetData.get_classification_Data,get_regression_Data
o	Prepare_Classification_Data.classification_data_prep
o	Prepare_Regression_Data.regression_data_prep
o	call_reg_class_models.call_classification_models
			Supplemental Python Program
			•	Classification_Models.Call_KNN_Classi
			•	Classification_Models.Call_Support_Vector_Classi
			•	Classification_Models.Call_QDA_Classi

o	call_reg_class_models.call_regression_models	
 		        Supplemental Python Program
			•	Regression_Models.Call_DecisionTree_Reg,
			•	Regression_Models.Call_Bagging_Reg,
			•	Regression_Models.Call_GradientBoosting_Reg
					Supplemental Python Program
					•	Regression_Plot.plot_model_complexity
					•	Regression_Plot.plot_model_learning
					•	Regression_Plot.plot_regression_predictions


		
o	dat_exploratory_plot.plot_exploration
	



