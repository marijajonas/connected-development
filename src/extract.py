from pathlib import Path
import pandas as pd

# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parents[1]

# Locate raw data
DATA_DIR = PROJECT_DIR / "data" / "raw"

# List our datasets
files = [
    "internet_users.csv",
    "gdp_per_capita.csv",
    "school_enrollment.csv"
]

print("Starting data extraction...")

for file in files:

    file_path = DATA_DIR / file

    print(f"\nReading: {file}")

    data = pd.read_csv(file_path)

    print("Dataset dimensions:", data.shape)

    print(data.head())