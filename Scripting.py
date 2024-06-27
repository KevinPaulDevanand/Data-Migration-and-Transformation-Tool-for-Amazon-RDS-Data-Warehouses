#Unziping and uploading the JSON file from the local system to AWS S3 bucket
from zipfile import ZipFile
import json
import boto3
import pandas as pd
with ZipFile("") as zObject:
    zObject.extractall(path="")
data=json.load(f)
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='',
    aws_access_key_id='',
    aws_secret_access_key=''
)
for bucket in s3.buckets.all():
    print(bucket.name)
s3.Bucket('kevintest1').upload_file(Filename=r'', Key='')
f.close()


#Lambda Function to automate flow of Data

import json
import boto3

def lambda_handler(event, context):
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    print(f"Bucket: {bucket_name}, Key: {object_key}")
    glue = boto3.client('glue')
    response = glue.start_job_run(
            JobName='',  # Replace with your Glue job name
            Arguments={
                '--bucket_name': bucket_name,
                '--object_key': object_key
            }
        )
        
    
    
    
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

