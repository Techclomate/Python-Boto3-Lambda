import boto3

session = boto3.Session(
    aws_access_key_id='AKIAY55PSKETWPYY7DBB',
    aws_secret_access_key='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'
)

# Create an S3 client using the session
s3 = session.client('s3')

# Get a list of all buckets
response = s3.list_buckets()

# Iterate through each bucket
for bucket in response['Buckets']:
    print(f"Contents of Bucket {bucket['Name']}:")
    # Get a list of all objects in the bucket
    objects = s3.list_objects(Bucket=bucket['Name'])
    # Iterate through each object
    for obj in objects['Contents']:
        print(f"\t{obj['Key']}")
