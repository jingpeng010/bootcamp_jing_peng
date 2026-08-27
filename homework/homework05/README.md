## Data Storage

This project separates raw and processed data into two folders:

- `data/raw/`: stores raw data in CSV format.
- `data/processed/`: stores processed data in Parquet format.

CSV is used for raw tabular data because it is simple, human-readable, and widely supported. Parquet is used for processed data because it is more storage-efficient, preserves data types, and supports efficient column-based reading.

File paths are configured using environment variables rather than hard-coded paths. The project uses `DATA_DIR_RAW` and `DATA_DIR_PROCESSED` from the `.env` file to define the raw and processed data directories.

Utility functions such as `write_df()` and `read_df()` detect the file format from the file extension and use the corresponding pandas read/write method.