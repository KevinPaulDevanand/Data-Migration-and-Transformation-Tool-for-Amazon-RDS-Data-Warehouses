import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
  
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
spark
import boto3
import pandas as pd
s3 = boto3.client('s3')
s3 = boto3.resource(
    service_name='s3',
    region_name='',
    aws_access_key_id='',
    aws_secret_access_key=''
)
for bucket in s3.buckets.all():
    print(bucket.name)
for obj in s3.Bucket('kevintest1').objects.all():
    print(obj)
obj = s3.Bucket('kevintest1').Object('iris.json').get()
data=pd.read_json(obj['Body'])
data.head()
spark_df=spark.createDataFrame(data)
spark_df.show()
spark_df.rdd.getNumPartitions()
spark_df_final=spark_df.repartition(1)
rds_endpoint = ""  # e.g., your-db-instance.123456789012.us-west-2.rds.amazonaws.com
rds_port = 3306  # Default MySQL port
rds_database = "test1"
mysql_url = f"jdbc:mysql://{rds_endpoint}:{rds_port}/{rds_database}"
table_name = "s3_datatest"
properties = {
    "user": "admin",
    "password": "kevin1999",
    "driver": "com.mysql.cj.jdbc.Driver"
}
spark_df_final.write.jdbc(url=mysql_url, table=table_name, mode='overwrite', properties=properties)
print("Data written successfully")
job.commit()
