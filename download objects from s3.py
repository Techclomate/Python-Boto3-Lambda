import boto3

# Provide AWS credentials
aws_access_key_id = 'AKIAY55PSKETWPYY7DBB'
aws_secret_access_key = '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'

# Create an S3 client with credentials
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Download a file from S3
s3.download_file('techclomate1', 'mountain.jpg', '/home/techclomate/images/mountain.jpg')
