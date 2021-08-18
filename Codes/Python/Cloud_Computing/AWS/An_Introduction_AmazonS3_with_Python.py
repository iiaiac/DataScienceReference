#!/usr/bin/env python
# coding: utf-8

# Reference : https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html 

# #### Activities in this module:
#     

# In[ ]:


# Installing Libraries
# pip install boto3
# pip install pandas
# pip install os


# In[ ]:


# Loading Libraries
import boto3
import pandas as pd
import os


# #### AWS Authentication

# In[ ]:


# S3 Credentials
AccesskeyID = 'xxxx'
Secretaccesskey = 'xxxx'


# In[ ]:


s3 = boto3.client("s3", 
                  aws_access_key_id=AccesskeyID, 
                  aws_secret_access_key=Secretaccesskey)


# #### Creating a bucket

# In[ ]:


bucket = s3.create_bucket(Bucket= '<Bucket_Name>')


# #### List of Existing Bucket

# In[ ]:


response = s3.list_buckets()


# In[ ]:


#Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


# #### List Bucket Content

# In[ ]:


s3.list_objects(Bucket='<Bucket_Name>')['Contents']


# #### Upload a File

# In[ ]:


file_path = r"YourFilePath"


# In[ ]:


s3.upload_file(file_path, '<Bucket_Name>', 'YourFileName')


# #### Download a file

# In[ ]:


s3.download_file('<Bucket_Name>', '<Bucket_Object_Name>', 'Local_File_Name')


# #### Delete a file from a bucket

# In[ ]:


s3.delete_object(Bucket='<Bucket_Name>', Key='object_name')


# #### Delete a bucket

# In[ ]:


s3.delete_bucket(Bucket='<Bucket_Name>')

