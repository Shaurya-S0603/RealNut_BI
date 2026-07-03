from pathlib import Path

from etl.importer import BlinkitImporter
from etl.validator import DataValidator
from etl.transformer import DataTransformer
from etl.loader import DataLoader

from database.db import engine

class ETLPipeline:

    def run(self, file_path: Path, table_name: str):

        importer = BlinkitImporter()

        validator = DataValidator()

        transformer = DataTransformer()

        loader = DataLoader()

        if file_path.suffix == ".csv":
            df = importer.read_csv(file_path)

        else:
            df = importer.read_excel(file_path)

        df = validator.validate(df)

        df = transformer.transform(df)

        loader.load(df, table_name, engine)