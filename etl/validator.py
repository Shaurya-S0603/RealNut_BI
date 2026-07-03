import pandas as pd

class DataValidator:

    @staticmethod
    def validate(df: pd.DataFrame):

        if df.empty:
            raise ValueError("File is empty.")

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return df