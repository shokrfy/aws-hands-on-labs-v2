# 💻 AWS S3 Lab: Management Console (GUI)

## 🎯 Objective

This lab provides a comprehensive, step-by-step guide on performing fundamental Amazon Simple Storage Service (S3) operations—specifically **creating a bucket** and **uploading an object**—using the **AWS Management Console**. This is the primary graphical user interface (GUI) method for interacting with AWS services.

---

## 🔑 Login and Navigation Steps

This section details the process of accessing the AWS Management Console and navigating to the Amazon S3 service dashboard.

| Step | Description | Screenshot |
| :--- | :--- | :--- |
| **1. Access the Login Page** | Navigate to the AWS Management Console login URL. Enter your **IAM User Name** and **Password** to sign in. | ![AWS Console Login Page](../../images/console-login-page.png) |
| **2. Navigate to the Console Home** | Upon successful login, you will be directed to the AWS Management Console Home dashboard. | ![AWS Console Main Dashboard](../../images/console-main-dashboard.png) |
| **3. Search for S3 Service** | Use the search bar at the top of the console to find and select the **S3** service. | *Refer to the search bar in the previous screenshot.* |
| **4. Access the S3 Dashboard** | This page provides an overview of the Amazon S3 service, including features and use cases. Click on **Buckets** or the **Create bucket** button to proceed. | ![AWS S3 Dashboard](../../images/images/console-s3-dashboard.png) |

---

## 🛠️ Lab Execution: Creating a Bucket and Uploading a CV

Follow these steps to create a new S3 bucket and securely upload the `Ahmed_Hossam_CV.pdf` file.

### Step 1: Create a New S3 Bucket

1.  **Initiate Bucket Creation:** Click the **Create bucket** button on the S3 dashboard.
2.  **Configure Bucket Settings:**
    *   **AWS Region:** Select your desired AWS Region (e.g., US East (N. Virginia) `us-east-1`).
    *   **Bucket Name:** Enter a globally unique name for your bucket (e.g., `ahmed-console-lab`).
    *   **Object Ownership:** For this lab, keep the default settings.
    *   **Block Public Access settings:** **Crucially**, ensure **Block all public access** is checked to maintain security.
3.  **Finalize Creation:** Scroll to the bottom and click the **Create bucket** button.

| Step Detail | Screenshot |
| :--- | :--- |
| **Bucket Creation Form** | ![AWS Console Create Bucket Form](../../images/console-create-bucket.png) |
| **Verification of Creation** | The new bucket (`ahmed-console-lab`) will now appear in your list of General purpose buckets. | ![AWS Console Bucket List](../../images/console-bucket-list.png) |

### Step 2: Upload the CV File

1.  **Select the Bucket:** Click on the newly created bucket (`ahmed-console-lab`) to open its details page.
2.  **Access Upload Interface:** Click the **Upload** button.
3.  **Add File:** On the upload page, click **Add files** and select the `Ahmed_Hossam_CV.pdf` file from your local machine.
4.  **Review and Upload:** Review the file details and click the **Upload** button at the bottom right.

| Step Detail | Screenshot |
| :--- | :--- |
| **Upload Page** | ![AWS Console Upload Page](../../images/console-upload-page.png) |
| **Upload Completion** | A status message will confirm the successful upload of the file. | ![AWS Console Upload Complete Status](../../images/console-upload-complete.png) |

### Step 3: Verify the Uploaded Object

1.  **View Object Details:** Navigate back to the bucket's main page. The `Ahmed_Hossam_CV.pdf` file will be listed as an object. Click on the object name.
2.  **Check Metadata:** The object details page confirms the file's properties, including the **Key** (file name), **Size**, **Storage class**, and **Content-Type** (`application/pdf`). This confirms the file is securely stored in S3.

| Step Detail | Screenshot |
| :--- | :--- |
| **Object Details Verification** | ![AWS Console Object Details](../../images/console-object-details.png) |

---

## 📝 Summary and References

### Summary Table

| Operation | Tool Used | Status | Notes |
| :--- | :--- | :--- | :--- |
| **Bucket Creation** | AWS Management Console | ✅ Success | Bucket name: `ahmed-console-lab` |
| **File Upload** | AWS Management Console | ✅ Success | File: `Ahmed_Hossam_CV.pdf` |
| **Verification** | AWS Management Console | ✅ Success | Object metadata confirmed. |

### References

| Resource | Description | Link |
| :--- | :--- | :--- |
| **Amazon S3 Documentation** | Official documentation for S3 features and pricing. | [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/) |
| **AWS Management Console** | Direct link to the AWS login page. | [https://aws.amazon.com/console/](https://aws.amazon.com/console/) |
| **S3 Best Practices** | Security and performance best practices for S3. | [https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/best-practices.html) |
