# ☁️ AWS Hands-on Labs: Amazon S3 Operations

## Project Overview

This repository contains a series of hands-on labs designed to demonstrate the fundamental operations of **Amazon Simple Storage Service (S3)**, the industry-leading object storage service. The labs focus on the core task of **creating an S3 bucket** and **uploading an object (a CV file)**, showcasing three distinct methods of interaction with the AWS platform.

This project is structured to provide a clear comparison between the different tools available to AWS users, from the graphical interface to programmatic access.

## 🚀 Labs Included

The project is divided into three comprehensive lab modules, each detailing the process using a different AWS access method:

| Module | Access Method | Description |
| :--- | :--- | :--- |
| **01-AWS-Console** | **AWS Management Console (GUI)** | A step-by-step guide using the web-based graphical interface. Ideal for beginners and manual operations. |
| **02-AWS-CLI** | **AWS Command Line Interface (CLI)** | Demonstrates using command-line tools for quick, scriptable, and efficient operations. |
| **03-AWS-SDK** | **AWS SDK (Python - Boto3)** | Shows how to programmatically interact with S3 using the official Python SDK, Boto3. Essential for application integration and automation. |

## 📁 Project Structure

The repository follows a clean, organized structure for easy navigation:

```
aws-hands-on-labs/
├── README.md                   <-- This file
├── Ahmed_Hossam_CV.pdf         <-- The sample file used for all upload labs
├── 01-AWS-Console/
│   └── console-lab.md          <-- Documentation for the GUI-based lab
├── 02-AWS-CLI/
│   └── cli-lab.md              <-- Documentation for the CLI-based lab
├── 03-AWS-SDK/
│   ├── sdk-lab.md              <-- Documentation for the Boto3-based lab
│   └── s3_lab.py               <-- The Python script used in the SDK lab
└── images/                     <-- All screenshots and visual assets
    ├── console-login-page.png
    ├── cli-configure.png
    └── ... (all other images)
```

## 💡 Key Takeaways

By completing these labs, you will gain practical experience in:

*   **S3 Fundamentals:** Understanding the concept of buckets and objects.
*   **Interface Proficiency:** Becoming comfortable with the AWS Console, CLI, and SDK.
*   **Automation vs. Manual:** Recognizing when to use a GUI for quick tasks versus a CLI/SDK for automation.
*   **Secure Operations:** Implementing best practices like blocking public access during bucket creation.

## 🔗 Resources

*   [Amazon S3 Official Documentation](https://aws.amazon.com/s3/)
*   [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/)
*   [AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/)
