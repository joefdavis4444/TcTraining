import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = "11252025batchtraining"
    key = "RawBronze/marvel_dc_actors (1).csv"

    try:
        # Read CSV from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Load into DataFrame
        df = pd.read_csv(StringIO(content))

        # Rename columns to snake_case
        df.rename(columns={
            "Movie": "movie",
            "Year": "year",
            "Main Actor": "main actor"

        }, inplace=True)

        # Save transformed CSV to buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Generate new key for output file
        output_key = f"StagingSilver/heromovies_actors.csv"

        # Upload the transformed file to S3
        s3.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=csv_buffer.getvalue()
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"File transformed and saved to {output_key}")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing file: {str(e)}")
        }
