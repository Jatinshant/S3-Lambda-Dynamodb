# S3-Lambda-Dynamodb
# 🚀 AWS CSV to DynamoDB Automation using Lambda and S3

This project demonstrates how to automatically import user data from a CSV file stored in an Amazon S3 bucket into a DynamoDB table using an AWS Lambda function. The Lambda function is triggered whenever a new CSV file is uploaded to the S3 bucket.

> 🧑‍💻 **Project developed by: [Jatin Shant]**

---

## 🔧 Tech Stack

- AWS Lambda (Python 3.9+)
- Amazon S3
- Amazon DynamoDB
- IAM Roles & Policies
- CloudWatch Logs

---

## 📁 Project Structure

```bash
project/
│
├── lambda_function.py     # Main Lambda function to parse CSV and store in DynamoDB
├── Dynamodb.csv           # Sample CSV file with user data
└── README.md              # This documentation file
```
## 📌 Use Case
Whenever a CSV file (e.g., Dynamodb.csv) is uploaded to the S3 bucket, the Lambda function automatically reads its contents and inserts each row as an item into the DynamoDB table.

## 🧾 Sample CSV Format
The CSV file should follow this structure:
user_id,email,first_name,last_name,age,city,country,subscription_type,created_date,last_login,is_active,purchase_count,total_spent
usr_001,john.doe@email.com,John,Doe,28,New York,USA,premium,2024-01-15,2024-06-20,true,5,299.99
📌 Make sure your file doesn't wrap rows in extra double quotes ("). Each line must be cleanly formatted like above.

### 🛠 Setup Instructions
## 1. 🔐 Create IAM Role for Lambda
Attach the following policies:
AmazonS3ReadOnlyAccess
AmazonDynamoDBFullAccess
Or create a custom policy with least privileges

## 2. ☁️ Create DynamoDB Table
Table name: users-table (or update it in the code)
Partition key: users_id (type: String)
✅ You may rename this to user_id if you also update the Lambda code to match

## 3. 🪣 Create an S3 Bucket
Name: Choose a unique name (e.g., your-bucket-name)
Enable event notification for ObjectCreated events
Connect the Lambda function as a trigger

## 4. 📦 Create the Lambda Function
Runtime: Python 3.9
Upload the code from lambda_function.py
Add an S3 trigger to invoke Lambda on file upload

## 5. ✅ Lambda Code: Where to Make Changes
Update these values as needed:
```
# DynamoDB table name
table_name = 'users-table'  # <- change this if your table name is different

# Change 'users_id' to 'user_id' if your table uses a different key
item = {
    'users_id': row['user_id'],  # <- match this to your DynamoDB table key
    }
```

## 🧪 Testing Locally (Optional)
If you're testing manually in the Lambda console, use this sample test event:
```
{
  "Records": [
    {
      "s3": {
        "bucket": {
          "name": "your-bucket-name"
        },
        "object": {
          "key": "Dynamodb.csv"
        }
      }
    }
  ]
}
```
🔁 Replace "your-bucket-name" and "Dynamodb.csv" with your actual bucket name and file name if different.

## 🧼 Troubleshooting
# KeyError: 'user_id' → Your CSV might have extra quotes or a malformed header. Use the cleaned version (Dynamodb_cleaned.csv).
# ValidationException (Missing key) → DynamoDB expects a partition key (users_id). Make sure you're matching the key name in both code and table.
# No Lambda trigger? → Ensure S3 trigger is correctly set and the file is not inside a folder in the bucket.

## 📄 License
MIT

## 🙌 Contributions Welcome
Feel free to fork, improve, or open issues for enhancements!

# 🧑‍💻 Author
# Made with ❤️ by Jatin Shant

---
Would you like a ZIP of this repo with the `lambda_function.py`, `Dynamodb_cleaned.csv`, and this `README.md` bundled together for upload to GitHub?
```
