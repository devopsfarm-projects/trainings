# Python + AWS Lambda File Processor

**Skills**: Python, AWS Lambda, S3, CloudWatch

**Tasks**:
- Create an S3 bucket to upload `.csv` files.
- Build a Python Lambda function triggered on `s3:ObjectCreated` events.
- Parse the CSV and generate summary logs (total rows, columns).
- Send logs to CloudWatch.
- (Bonus) Notify via SNS on upload.