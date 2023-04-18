import boto3

# Set up AWS credentials
session = boto3.Session(
    aws_access_key_id='AKIAY55PSKETWPYY7DBB',
    aws_secret_access_key='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',
    region_name='us-east-1'
)

# Create an S3 client
s3 = session.client('s3')

# List all objects in the bucket
objects = s3.list_objects_v2(Bucket='techclomate1')

# Write object keys to a text file
with open('object_keys.txt', 'w') as f:
    for obj in objects['Contents']:
        f.write(obj['Key'])
