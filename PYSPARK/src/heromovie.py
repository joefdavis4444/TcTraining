import json
import boto3
from datetime import datetime
from io import StringIO
import pandas as pd

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = "11252025batchtraining"
    key = "RawBronze/dc_marvel_movie_performance.csv"

    try:
        # Read CSV from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Load into DataFrame
        df = pd.read_csv(StringIO(content))

        # Rename columns to snake_case
        df.rename(columns={
            "Film": "film",
            "U.S. release date": "us_release_date",
            "Box office gross Domestic (U.S. and Canada )": "domestic_gross",
            "Box office gross Other territories": "international_gross",
            "Box office gross Worldwide": "worldwide_gross",
            "Budget": "budget",
            "MCU": "mcu",
            "Phase": "phase",
            "Distributor": "distributor",
            "MPAA Rating": "mpaa_rating",
            "Length": "length",
            "Minutes": "minutes",
            "Franchise": "franchise",
            "Character Family": "character_family",
            "Domestic %": "pct_domestic",
            "Gross to Budget": "gross_to_budget",
            "Rotten Tomatoes Critic Score": "critics_score_pct",
            "Male/Female-led": "lead_gender",
            "Year": "year",
            "Inflation Adjusted Worldwide Gross": "inflation_adjusted_worldwide_gross",
            "Inflation Adjusted Budget": "inflation_adjusted_budget",
            "2.5x prod": "prod_2_5x",
            "Break Even": "break_even"
        }, inplace=True)

        # Save transformed CSV to buffer
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)

        # Generate new key for output file
        output_key = f"StagingSilver/heromovies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

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
