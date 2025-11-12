# ⚙️ AWS S3 Lab: Command Line Interface (CLI)

## 🎯 Objective

This lab demonstrates how to interact with Amazon S3 using the **AWS Command Line Interface (CLI)**. The CLI is a unified tool to manage your AWS services from the command line, allowing for powerful scripting and automation. We will cover configuration, bucket creation, and object upload.

---

## 🔑 Setup and Authentication

Before executing S3 commands, the AWS CLI must be installed and configured with your credentials.

### Step 1: Configure AWS Credentials

Use the `aws configure` command to set up your **Access Key ID**, **Secret Access Key**, default **Region**, and **Output Format**. These credentials are used by the CLI to authenticate your requests.

| Step Detail | Screenshot |
| :--- | :--- |
| **CLI Configuration** | The command prompts for your credentials and default settings. | ![AWS CLI Configure](../../images/cli-configure.png) |

```bash
$ aws configure
AWS Access Key ID [****************RSM4]: AKIA...
AWS Secret Access Key [****************Vck]: k7hR...
Default region name [None]: us-east-1
Default output format [None]: json
```

### Step 2: Create a New S3 Bucket

The `aws s3 mb` (make bucket) command is used to create a new bucket. The bucket name must be globally unique.

| Step Detail | Screenshot |
| :--- | :--- |
| **Bucket Creation Command** | The command `aws s3 mb s3://ahmed-cli-lab` creates the bucket. | ![AWS CLI Create Bucket](../../images/cli-create-bucket.png) |

```bash
$ aws s3 mb s3://ahmed-cli-lab
make_bucket: ahmed-cli-lab
```

### Step 3: Upload the CV File

The `aws s3 cp` (copy) command is used to upload a local file to an S3 bucket. The command syntax is similar to a standard file copy operation.

| Step Detail | Screenshot |
| :--- | :--- |
| **File Upload Command** | The command copies the local file `Ahmed_Hossam_CV.pdf` to the target S3 path. | ![AWS CLI Upload CV](../../images/cli-upload-cv.png) |

```bash
$ aws s3 cp Ahmed_Hossam_CV.pdf s3://ahmed-cli-lab/
upload: .\Ahmed_Hossam_CV.pdf to s3://ahmed-cli-lab/Ahmed_Hossam_CV.pdf
```

### Step 4: Verify the Uploaded Object

The `aws s3 ls` (list) command is used to list the contents of an S3 bucket, confirming the file was uploaded successfully.

| Step Detail | Screenshot |
| :--- | :--- |
| **Verification Command** | The output shows the file size and name, confirming its presence in the bucket. | ![AWS CLI List Bucket After Upload](../../images/cli-list-bucket-after-upload.png) |

```bash
$ aws s3 ls s3://ahmed-cli-lab/
2025-11-12 17:04:32      95050 Ahmed_Hossam_CV.pdf
```

---

## 📝 Summary and References

### Summary Table

| Operation | Tool Used | Command | Status |
| :--- | :--- | :--- | :--- |
| **Configuration** | AWS CLI | `aws configure` | ✅ Success |
| **Bucket Creation** | AWS CLI | `aws s3 mb` | ✅ Success |
| **File Upload** | AWS CLI | `aws s3 cp` | ✅ Success |
| **Verification** | AWS CLI | `aws s3 ls` | ✅ Success |

### References

| Resource | Description | Link |
| :--- | :--- | :--- |
| **AWS CLI Documentation** | Official documentation for installing and using the AWS CLI. | [https://aws.amazon.com/cli/](https://aws.amazon.com/cli/) |
| **S3 CLI Command Reference** | Detailed reference for all `aws s3` commands. | [https://docs.aws.amazon.com/cli/latest/reference/s3/](https://docs.aws.amazon.com/cli/latest/reference/s3/) |
| **Configuring the AWS CLI** | Guide on setting up credentials and configuration files. | [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) |
