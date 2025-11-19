import json
import boto3
import pandas as pd
from io import StringIO

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Processing file: {key} from bucket: {bucket}")

    # Read CSV from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(response['Body'])

    # Transform column names to Silver schema
    df.columns = [
        "Film", "U.S. release date", "Box office gross Domestic (U.S. and Canada )",
        "Box office gross Other territories", "Box office gross Worldwide", "Budget", "MCU", "Phase",
        "Distributor", "MPAA Rating", "Length", "Minutes", "Franchise", "Character Family",
        "Domestic %", "Gross to Budget", "Rotten Tomatoes Critic Score", "Male/Female-led", "Year",
        "Inflation Adjusted Worldwide Gross", "Inflation Adjusted Budget", "2.5x prod", "Break Even"
    ]

    # Send each row as JSON to Kinesis
    for _, row in df.iterrows():
        record = row.to_dict()
        kinesis.put_record(
            StreamName='heromoviestream',
            Data=json.dumps(record),
            PartitionKey=str(row.get("Film", "unknown"))
        )

    print(f"Successfully sent {len(df)} records to Kinesis stream: heromoviestream")

    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully processed {key} and sent {len(df)} records to Kinesis')
    }
