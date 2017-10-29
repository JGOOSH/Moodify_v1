import boto3
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version='s3v4'))

data = open('face.jpg', 'rb')
s3.Bucket('azureemotion992').put_object(Key='face.jpg', Body = data)

url = s3.generate_presigned_url(
    ClientMethod='get_object' ,
    Params={
        'Bucket' : 'azureemotion992',
        'Key' : 'face.jpg'
    }
)
