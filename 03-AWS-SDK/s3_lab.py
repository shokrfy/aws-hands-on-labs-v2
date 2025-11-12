import boto3
import os
from botocore.exceptions import ClientError

# --- Configuration ---
# The bucket name should be unique globally. Using a dynamic name with a timestamp is recommended.
BUCKET_NAME = "ahmed-sdk-lab-2025-01" # Replace with your unique bucket name
FILE_TO_UPLOAD = "Ahmed_Hossam_CV.pdf"
REGION = "us-east-1" # Replace with your desired region

# Initialize S3 client
s3_client = boto3.client('s3', region_name=REGION)

def list_buckets():
    """Lists all S3 buckets in the account."""
    print("Listing buckets in account:")
    try:
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            print(f" - {bucket['Name']}")
    except ClientError as e:
        print(f"Error listing buckets: {e}")

def create_bucket(bucket_name, region):
    """Creates an S3 bucket in the specified region."""
    try:
        if region == 'us-east-1':
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration={'LocationConstraint': region})
        print(f"Bucket created: {bucket_name}")
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            print(f"Bucket '{bucket_name}' already exists and is owned by you.")
        elif e.response['Error']['Code'] == 'BucketAlreadyExists':
            print(f"Bucket '{bucket_name}' already exists (globally unique name violation).")
        else:
            print(f"Error creating bucket: {e}")
        return False
    return True

def upload_file(file_name, bucket, object_name=None):
    """Uploads a file to an S3 bucket."""
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded: {file_name} -> s3://{bucket}/{object_name}")
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False
    return True

def list_objects(bucket_name):
    """Lists objects in a specified S3 bucket."""
    print(f"\nObjects in bucket {bucket_name}:")
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if response['KeyCount'] == 0:
            print(" (Bucket is empty)")
        else:
            for obj in response['Contents']:
                print(f" - {obj['Key']} (size={obj['Size']})")
    except ClientError as e:
        print(f"Objects list error (maybe empty or access issue): An error occurred ({e.response['Error']['Code']}) when calling the ListObjectsV2 operation: {e.response['Error']['Message']}")

def generate_presigned_url(bucket_name, object_key, expiration=600):
    """Generates a presigned URL to share an S3 object."""
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_key},
                                                    ExpiresIn=expiration)
        print(f"\nPresigned URL (valid for {expiration} seconds):")
        print(response)
        print("\n(You can open the presigned URL in a browser to download the file.)")
    except ClientError as e:
        print(f"Error generating presigned URL: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    print("--- AWS SDK (Python - Boto3) Lab Execution ---")

    # 1. List existing buckets
    list_buckets()

    # 2. Create a new bucket
    create_bucket(BUCKET_NAME, REGION)

    # 3. Upload the CV file
    # Note: The script assumes Ahmed_Hossam_CV.pdf is in the current working directory or accessible path.
    # For this lab, we assume the user will run the script from the root of the project where the CV file is located.
    upload_file(f"../{FILE_TO_UPLOAD}", BUCKET_NAME)

    # 4. Verify the upload by listing objects
    list_objects(BUCKET_NAME)

    # 5. Generate a presigned URL for the uploaded object
    generate_presigned_url(BUCKET_NAME, FILE_TO_UPLOAD)

    print("\n--- Lab Execution Complete ---")
