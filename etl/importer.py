from pathlib import Path
import pandas as pd

class BlinkitImporter:

    def read_excel(self, file_path: Path):

        print(f"Reading {file_path.name}")
        return pd.read_excel(file_path)

    def read_csv(self, file_path: Path):

        print(f"Reading {file_path.name}")
        return pd.read_csv(file_path)