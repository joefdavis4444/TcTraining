import json
import boto3
import base64
from decimal import Decimal
import math

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('heromovies')
sns = boto3.client('sns')
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-1:430006376054:HeroTopic'


def lambda_handler(event, context):
    inserted_count = 0

    for record in event['Records']:
        # Decode Kinesis payload
        payload = record['kinesis']['data']
        data = json.loads(base64.b64decode(payload))

        sanitized_data = {}
        for k, v in data.items():
            if isinstance(v, float):
                sanitized_data[k] = Decimal('0') if math.isnan(v) or math.isinf(v) else Decimal(str(v))
            elif isinstance(v, int):
                sanitized_data[k] = Decimal(v)
            else:
                sanitized_data[k] = v

        # Insert into DynamoDB
        table.put_item(Item=sanitized_data)
        inserted_count += 1

        # Prepare SNS message
        film = sanitized_data.get('Film', 'Unknown')
        gross = sanitized_data.get('Box office gross Worldwide', 0)

        message = {
            'film': film,
            'gross': str(gross),
            'note': f"🎬 New movie record added: {film}"
        }

        # Publish to SNS topic
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"New Hero Movie Added: {film}",
            Message=json.dumps(message, indent=2)
        )

    print(f"Inserted {inserted_count} items into DynamoDB.")

    return {
        'statusCode': 200,
        'body': json.dumps(f"Processed {inserted_count} records from Kinesis.")
    }
