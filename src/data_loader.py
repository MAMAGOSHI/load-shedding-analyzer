import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from src.exceptions import MissingDataError

DATASET = "sbonelondhlazi/sa-electricity-historical-data"
FILE_NAME = "EskomSePush_history.csv"
RAW_PATH = "data/raw"


def download_dataset():
    """
    Download dataset from Kaggle API.
    """

    os.makedirs(RAW_PATH, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(
        DATASET,
        path=RAW_PATH,
        unzip=True
    )

    print("Dataset downloaded successfully.")


def load_data():
    """
    Load CSV into pandas DataFrame.
    """

    file_path = os.path.join(RAW_PATH, FILE_NAME)

    if not os.path.exists(file_path):
        raise MissingDataError(
            f"Dataset not found at {file_path}"
        )

    df = pd.read_csv(file_path)

    return df
