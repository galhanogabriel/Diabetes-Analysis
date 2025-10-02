from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parents[2]

DATA_FOLDER = PROJECT_FOLDER / "dados" # Data folder

# Place the path to your project's data files below
ORIGINAL_DATA = DATA_FOLDER / "diabetes.csv"
PROCESSED_DATA = DATA_FOLDER / "diabetes_processed.parquet"