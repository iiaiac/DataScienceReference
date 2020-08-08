# Reference : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

# #### Activities in this module:

# Installing Libraries
 pip install boto3
 pip install pandas
 pip install os

# Loading Libraries
import boto3
import pandas as pd
import os


# #### AWS Authentication

# S3 Credentials
AccesskeyID = 'AKIA56ZNHXD4KS4YNVWP'
Secretaccesskey = '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'
s3 = boto3.client("s3", 
                  aws_access_key_id=AccesskeyID, 
                  aws_secret_access_key=Secretaccesskey)


# #### Creating a bucket
bucket = s3.create_bucket(Bucket= 'sgsanalytics')

# #### List of Existing Bucket
response = s3.list_buckets()

# #### List Bucket Content
s3.list_objects(Bucket='sgsanalytics')['Contents']

#Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


# #### Upload a File
file_path = r"C:\Users\Anant Awasthi\Google Drive\SSCR India\sscr.ai\Stakeholders.xlsx"
s3.upload_file(file_path, 'sgsanalytics', 'Dir1/Stakeholders.xlsx')

# #### Download a file
s3.download_file('sgsanalytics', 'Stakeholders.xlsx', 'Stakeholders_downloaded_version.xlsx')

# #### Delete a file from a bucket
s3.delete_object(Bucket='sgsanalytics', Key='Stakeholders.xlsx')

# #### Delete a bucket
s3.delete_bucket(Bucket='sgsanalytics')

