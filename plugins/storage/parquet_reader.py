import pandas as pd
from typing import Dict, Generator

class ParquetReader:

    def __init__(self, file_path: str, batch_size: int = 10000):
        self.file_path = file_path
        self.batch_size = batch_size

    def stream_records(self) -> Generator[Dict, None, None]:
        for chunk in pd.read_parquet(self.file_path, chunksize=self.batch_size):
            for record in chunk.to_dict(orient="records"):
                yield record
