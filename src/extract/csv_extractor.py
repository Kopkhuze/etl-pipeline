"""
CSV Extractor
Reads the Crashes data from the NYC Open Data website from a local CSV file into a pandas DataFrame.
"""

import pandas as pd
from pathlib import Path

def extract_from_csv(file_path):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f'File not found: {path}')

    if path.stat().st_size == 0:
        raise ValueError(f'CSV file empty: {path}')

    print(f"[CSV Extractor] Reading: {path.name}")

    df = pd.read_csv(path)

    print(f"[CSV Extractor] Loaded {len(df):,} rows and {len(df.columns)} columns")

    return df

if __name__ == "__main__":
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    sample_path = root / "data" / "raw" / "crashes_data.csv"
    df = extract_from_csv(sample_path)
    print(df.head())