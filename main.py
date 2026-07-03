from pathlib import Path
from etl.pipeline import ETLPipeline

pipeline = ETLPipeline()

pipeline.run(
    Path("data/raw/sales.xlsx"),
    "sales"
)