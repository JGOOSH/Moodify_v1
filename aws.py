import boto3
from botocore.client import Config
import requests

s3 = boto3.resource('s3')

# for bucket in s3.buckets.all():
#     print(bucket.name)

data = open('face.jpg', 'rb')
s3.Bucket('azureemotion992').put_object(Key='face.jpg', Body = data)

# s3 = boto3.client('s3', config=Config(signature_version='s3v4'))

# url = s3.generate_presigned_url(
#     ClientMethod='get_object' ,
#     Params={
#         'Bucket' : 'azureemotion992',
#         'Key' : 'face.jpg'
#     }
# )

import boto.s3
conn = boto.s3.connect_to_region('us-east-2')  # or region of choice
bucket = conn.get_bucket('azureemotion992')
key = bucket.lookup('face.jpg')
key.set_acl('public-read')
