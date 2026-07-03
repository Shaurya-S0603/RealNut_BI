from sqlalchemy.orm import Session
class DataLoader:

    @staticmethod
    def load(df, table_name, engine):

        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )
        print(f"Inserted {len(df)} rows")