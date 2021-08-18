
# Task of the day : Data Import in Python
# Datasets : http://d3analytics.co.in/datasets/athelete_dataset/
# Library used Pandas 

""" ****************************************************************************************** """

# Loading Libraries 
import pandas as pd

# Reading a CSV file
csv_data = pd.read_csv('http://d3analytics.co.in/datasets/athelete_dataset/Athelete_Data.csv')

# Reading a Text file
text_data = pd.read_csv('http://d3analytics.co.in/datasets/athelete_dataset/Athelete_Data.txt', delimiter="\t")

# Reading an excel file
excel_data = pd.read_excel('http://d3analytics.co.in/datasets/athelete_dataset/Athelete_Data.xlsx')

# Reading a SAS (*.sas7bdat) file
sas_data = pd.read_sas('http://d3analytics.co.in/datasets/athelete_dataset/Athelete_Data.sas7bdat', \
                       format = 'sas7bdat', encoding="iso-8859-1")

