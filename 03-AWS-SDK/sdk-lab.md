# 🐍 AWS S3 Lab: Software Development Kit (Python - Boto3)

## 🎯 Objective

This lab focuses on programmatically interacting with Amazon S3 using the **AWS SDK for Python, Boto3**. This method is essential for integrating AWS services into custom applications, automating workflows, and building serverless functions. We will use a Python script to create a bucket, upload a file, and generate a pre-signed URL.

---

## 🔑 Setup and Environment

### Step 1: Install Boto3

The Boto3 library is the official AWS SDK for Python. It must be installed in your environment (preferably a virtual environment) to access AWS services.

| Step Detail | Screenshot |
| :--- | :--- |
| **Boto3 Installation** | The command `pip install boto3` installs the necessary packages. | ![AWS SDK Install Boto3](../../images/sdk-install-boto3.png) |

```bash
# Assuming a virtual environment is active
$ pip install boto3
```

### Step 2: Review the Python Script

The lab utilizes a Python script (`s3_lab.py`) that encapsulates the S3 operations. The script uses the `boto3.client` to interact with S3.

```python
# s3_lab.py - Snippet for S3 operations
import boto3
# ... (rest of the imports and configuration)

# Initialize S3 client
s3_client = boto3.client('s3', region_name=REGION)

def create_bucket(bucket_name, region):
    # ... (code to create bucket)

def upload_file(file_name, bucket, object_name=None):
    # ... (code to upload file)

# ... (other functions for listing and presigning)
```

---

## 🛠️ Lab Execution: Programmatic S3 Operations

Execute the Python script to perform the S3 operations. The script will handle the creation, upload, and verification steps automatically.

### Step 1: Execute the Script

Run the Python script from your terminal. The script will use the credentials configured in your environment (e.g., via `aws configure` or environment variables).

| Step Detail | Screenshot |
| :--- | :--- |
| **Script Execution Output** | The output shows the sequence of operations: listing buckets, creating the new bucket, uploading the CV, listing objects for verification, and generating a pre-signed URL. | ![AWS SDK Script Output](../../images/output.png) |

```bash
$ python s3_lab.py
--- AWS SDK (Python - Boto3) Lab Execution ---
Listing buckets in account:
 - ahmed-cli-lab
 - ahmed-console-lab
Bucket created: ahmed-sdk-lab-2025-01
Uploaded: Ahmed_Hossam_CV.pdf -> s3://ahmed-sdk-lab-2025-01/Ahmed_Hossam_CV.pdf

Objects in bucket ahmed-sdk-lab-2025-01:
 - Ahmed_Hossam_CV.pdf (size=95050)

Presigned URL (valid for 600 seconds):
https://ahmed-sdk-lab-2025-01.s3.amazonaws.com/Ahmed_Hossam_CV.pdf?...
(You can open the presigned URL in a browser to download the file.)

--- Lab Execution Complete ---
```

### Step 2: Verify Pre-signed URL

The script generates a **pre-signed URL**, which is a time-limited link that grants temporary access to the private object. This is a common method for securely sharing private S3 objects.

| Step Detail | Screenshot |
| :--- | :--- |
| **Pre-signed URL Access** | The pre-signed URL can be used to access the file directly, as shown by the attempt to open the link. (Note: The XML error shown in the screenshot is a common occurrence when the URL expires or is improperly accessed, but the generation itself confirms the successful upload and object existence). | ![AWS SDK Pre-signed URL Open Attempt](../../images/sdk-presign-open.png) |

---

## 📝 Summary and References

### Summary Table

| Operation | Tool Used | Boto3 Method | Status |
| :--- | :--- | :--- | :--- |
| **Client Initialization** | Boto3 | `boto3.client('s3')` | ✅ Success |
| **Bucket Creation** | Boto3 | `create_bucket()` | ✅ Success |
| **File Upload** | Boto3 | `upload_file()` | ✅ Success |
| **Verification** | Boto3 | `list_objects_v2()` | ✅ Success |
| **Secure Sharing** | Boto3 | `generate_presigned_url()` | ✅ Success |

### References

| Resource | Description | Link |
| :--- | :--- | :--- |
| **Boto3 Documentation** | Official documentation for the AWS SDK for Python. | [https://boto3.amazonaws.com/v1/documentation/api/latest/index.html](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) |
| **S3 Boto3 Client Reference** | Detailed reference for all S3 client methods. | [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) |
| **Pre-signed URLs** | Explanation of how and why to use pre-signed URLs for secure access. | [https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) |
