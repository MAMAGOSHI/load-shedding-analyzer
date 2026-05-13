import pandas as pd
from src.exceptions import InvalidStageError


class DataCleaner:

    def __init__(self, df):
        self.df = df

    def process(self):
        """
        Clean and validate data.
        """

        # remove duplicates
        self.df = self.df.drop_duplicates()

        # remove missing rows
        self.df = self.df.dropna()

        # convert datetime
        self.df["datetime"] = pd.to_datetime(
            self.df["datetime"],
            errors="coerce"
        )

        # remove invalid dates
        self.df = self.df.dropna(subset=["datetime"])

        # make sure stage column exists
        if "stage" not in self.df.columns:
            raise InvalidStageError(
                "Missing stage column."
            )

        # ensure stage values are numeric
        self.df["stage"] = pd.to_numeric(
            self.df["stage"],
            errors="coerce"
        )

        # remove invalid stages
        self.df = self.df.dropna(subset=["stage"])

        return self.df