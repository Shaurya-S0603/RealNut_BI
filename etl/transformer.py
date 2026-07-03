import pandas as pd

class DataTransformer:

    @staticmethod
    def transform(df: pd.DataFrame):

        df = df.copy()
        return df