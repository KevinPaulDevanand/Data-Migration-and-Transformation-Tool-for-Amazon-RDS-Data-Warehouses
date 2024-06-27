# Data-Migration-and-Transformation-Tool-for-Amazon-RDS-Data-Warehouses

To extract the data from a zip file that is available at a URL and load it into Amazon S3 and Amazon RDS (NoSQL), you can follow these steps: 
Use the requests library to download the zip file from the URL.
Use the zipfile module to extract the data from the zip file.
Use the boto3 library to store the data in Amazon S3.
Use the pandas library and  PySpark to load the data from S3 into Amazon RDS 

Unzip and Upload Data to S3:

Unzipped the file to obtain the JSON data.
Used a Python script to upload the JSON file to an Amazon S3 bucket.
Invoke Lambda Function:

Configured S3 to trigger an AWS Lambda function upon the upload of the JSON file.
Ensured the Lambda function is set up to handle the incoming S3 event.
Trigger AWS Glue Job:

The Lambda function triggered an AWS Glue job.
The AWS Glue job is written in PySpark to handle the data transformation process.
Transform Data in AWS Glue:

The Glue job read the JSON file from the S3 bucket.
The JSON data was transformed into a PySpark DataFrame.
Performed necessary data transformations and cleaning.
Load Data into Amazon RDS:

The transformed data was written from the PySpark DataFrame to a table in Amazon RDS.
Ensured the data was correctly formatted and inserted into the appropriate database schema.
Monitor and Validate:

Monitored the entire process to ensure successful completion.
Validated the data in Amazon RDS to ensure accuracy and completeness.
