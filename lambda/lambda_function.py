import os
import csv
import io
import json
import logging
from datetime import datetime, timedelta

import boto3
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)

FOOTBALL_DATA_API_KEY = os.environ["FOOTBALL_DATA_API_KEY"]
S3_BUCKET = os.environ["S3_BUCKET"]
COMPETITION_CODE = "PL"
LOOKBACK_DAYS = int(os.environ.get("LOOKBACK_DAYS", "3"))

s3_client = boto3.client("s3")


def fetch_recent_finished_matches():
    """Call football-data.org for PL matches finished in the last LOOKBACK_DAYS."""
    date_to = datetime.utcnow().date()
    date_from = date_to - timedelta(days=LOOKBACK_DAYS)

    url = f"https://api.football-data.org/v4/competitions/{COMPETITION_CODE}/matches"
    headers = {"X-Auth-Token": FOOTBALL_DATA_API_KEY}
    params = {
        "dateFrom": date_from.isoformat(),
        "dateTo": date_to.isoformat(),
        "status": "FINISHED",
    }

    response = requests.get(url, headers=headers, params=params, timeout=30)
    response.raise_for_status()
    return response.json()["matches"]


def matches_to_csv_bytes(matches):
    """Convert the raw matches JSON list into CSV bytes, mirroring raw_matches.csv shape."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow([
        "id", "utcDate", "status", "matchday", "season",
        "home_team_id", "home_team_name", "away_team_id", "away_team_name",
        "home_goals", "away_goals", "winner",
    ])

    for m in matches:
        writer.writerow([
            m["id"],
            m["utcDate"],
            m["status"],
            m["matchday"],
            m["season"]["startDate"][:4],
            m["homeTeam"]["id"],
            m["homeTeam"]["name"],
            m["awayTeam"]["id"],
            m["awayTeam"]["name"],
            m["score"]["fullTime"]["home"],
            m["score"]["fullTime"]["away"],
            m["score"]["winner"],
        ])

    return buffer.getvalue().encode("utf-8")


def lambda_handler(event, context):
    matches = fetch_recent_finished_matches()
    logger.info(f"Fetched {len(matches)} finished matches from the last {LOOKBACK_DAYS} days")

    if not matches:
        logger.info("No new finished matches in this window — nothing to upload")
        return {"statusCode": 200, "body": json.dumps({"matches_found": 0})}

    csv_bytes = matches_to_csv_bytes(matches)
    run_date = datetime.utcnow().strftime("%Y-%m-%d")
    key = f"raw/raw_matches_incremental/{run_date}/matches.csv"

    s3_client.put_object(Bucket=S3_BUCKET, Key=key, Body=csv_bytes)
    logger.info(f"Uploaded {len(matches)} matches to s3://{S3_BUCKET}/{key}")

    return {"statusCode": 200, "body": json.dumps({"matches_found": len(matches), "s3_key": key})}