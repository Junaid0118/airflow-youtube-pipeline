# YouTube Trending Data ETL Pipeline

**Author:** Junaid Iqbal shah  
**Tech Stack:** Python, Airflow, Pandas, SQLAlchemy, PostgreSQL, Parquet, YouTube Data API  
**Project Type:** ETL / Data Engineering Portfolio Project  

---

## Project Overview

This project is a **scalable ETL pipeline** built with **Apache Airflow** that extracts trending videos data from the **YouTube Data API**, transforms the data, stores it in **CSV/Parquet**, and finally loads it into a **PostgreSQL database**.  

It demonstrates **best practices in data engineering**, including:

- Modular and reusable code using **Single Responsibility Principle (SRP)**.  
- Efficient handling of **large datasets (1TB+)** using **streaming, batching, and Parquet format**.  
- Production-ready Airflow DAGs with logging, retries, and proper error handling.  
- PostgreSQL integration using **SQLAlchemy ORM** with batch inserts.  

---

## Project Architecture

```mermaid
flowchart TD
    A[YouTube API] --> B[Fetcher: YouTubeDataFetcher]
    B --> C[Transformer: YouTubeDataTransformer]
    C --> D[CSV / Parquet Storage]
    D --> E[PostgreSQL Storage: PostgresWriter]
    E --> F[Analytics / Dashboard / Queries]
