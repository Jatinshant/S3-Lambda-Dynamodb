import boto3
import csv
from decimal import Decimal

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'users-table'
table = dynamodb.Table(table_name)

def parse_boolean(value):
    return value.lower() == 'true'

def lambda_handler(event, context):
    # Get S3 object info from the event
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
    except Exception as e:
        return {"statusCode": 400, "body": f"Invalid event structure: {str(e)}"}

    try:
        # Fetch CSV file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8').splitlines()
        reader = csv.DictReader(content)

        successful = 0
        failed = 0

        for row in reader:
            try:
                # Convert data types
                item = {
                    'users_id': row['user_id'],
                    'email': row['email'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'age': int(row['age']),
                    'city': row['city'],
                    'country': row['country'],
                    'subscription_type': row['subscription_type'],
                    'created_date': row['created_date'],
                    'last_login': row['last_login'],
                    'is_active': parse_boolean(row['is_active']),
                    'purchase_count': int(row['purchase_count']),
                    'total_spent': Decimal(row['total_spent'])
                }

                table.put_item(Item=item)
                successful += 1
            except Exception as e:
                print(f"Error processing row {row}: {e}")
                failed += 1

        return {
            "statusCode": 200,
            "body": f"CSV processed. Success: {successful}, Failed: {failed}",
            "bucket": bucket,
            "file": key
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Failed to read CSV from S3: {str(e)}"
        }
