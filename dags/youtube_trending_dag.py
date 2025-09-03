import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)


from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from plugins.fetcher.youtube_fetcher import YouTubeDataFetcher
from plugins.transformer.youtube_transformer import YouTubeDataTransformer
from plugins.storage.csv_storage import CSVStorage
from plugins.storage.psql_writer import PostgresWriter

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": True,
    "email": ["alerts@yourdomain.com"],
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

# --------------------------
# Task 1: Fetch & Store CSV
# --------------------------
def fetch_transform_store_csv(**kwargs):
    fetcher = YouTubeDataFetcher()
    transformer = YouTubeDataTransformer()
    storage = CSVStorage()

    try:
        for raw in fetcher.get_video_stream():
            record = transformer.transform(raw)
            record["engagement_rate"] = (
                float(record.get("like_count", 0) or 0) /
                max(int(record.get("view_count", 1)), 1)
            )
            storage.write(record)
    finally:
        storage.close()

# --------------------------
# Task 2: Read CSV → Store PSQL
# --------------------------
def csv_to_psql(**kwargs):
    writer = PostgresWriter()
    import pandas as pd

    df = pd.read_csv("data/youtube_trending.csv")
    for record in df.to_dict(orient="records"):
        writer.write(record)
    writer.close()


# --------------------------
# DAG Definition
# --------------------------
with DAG(
    "youtube_trending_pipeline",
    default_args=default_args,
    description="ETL: YouTube API → CSV → PostgreSQL",
    schedule_interval="@daily",
    start_date=datetime(2025, 9, 4),
    catchup=False,
    tags=["youtube", "etl"],
) as dag:

    task_fetch_csv = PythonOperator(
        task_id="fetch_transform_store_csv",
        python_callable=fetch_transform_store_csv,
        provide_context=True
    )

    task_csv_to_psql = PythonOperator(
        task_id="csv_to_psql",
        python_callable=csv_to_psql,
        provide_context=True
    )

    task_fetch_csv >> task_csv_to_psql
