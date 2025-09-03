import os
import pandas as pd
from typing import Dict, List
import config

class ParquetStorage:

    def __init__(self):
        self.output_file = config['OUTPUT_FILE'].replace(".csv", ".parquet")
        os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        self._buffer: List[Dict] = []

        self._initialized = os.path.exists(self.output_file)

    def write(self, record: Dict):
        self._buffer.append(record)

        if len(self._buffer) >= 10_000:
            self.flush()

    def flush(self):
        if not self._buffer:
            return

        df = pd.DataFrame(self._buffer)

        df.to_parquet(
            self.output_file,
            engine="pyarrow",
            index=False,
            compression="snappy",
            append=self._initialized
        )

        self._initialized = True
        self._buffer.clear()

    def close(self):
        self.flush()
