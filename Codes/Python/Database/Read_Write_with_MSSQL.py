
# Import Libraries
import pyodbc
import pandas as pd
import sqlalchemy as sa
from sqlalchemy import create_engine

# Share Database Details
database_server = 'database_server'
username = 'username'
password = 'password'
database_name = 'database_name'
table_name = 'table_name'

# Create an SQL Engine
engine = sa.create_engine('mssql+pyodbc://' + username + ':' + password + '@' + database_server + '/' + database_name+'?DRIVER={SQL Server Native Client 11.0}')

# Reading Data to upload to Server
rdata = pd.read_excel('http://d3analytics.co.in/datasets/athelete_dataset/Athelete_Data.xlsx')

# Writing Data to SQL Server
rdata.to_sql(table_name, con = engine, if_exists = 'replace')

# Reading Data from SQL Server
sql = 'select count(*) from table'
data = pd.read_sql(sql)

# *************************************************************************************
