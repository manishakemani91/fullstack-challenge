import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    Table,
    String,
    Float,
    BigInteger,
    inspect,
)
from sqlalchemy.sql import text
from sqlalchemy.types import VARCHAR, Float as SQLAlchemyFloat


load_dotenv(".env")
# Define the path to the Excel file and the SQLite database
excel_file = "data.xlsx"

# Create a connection to the Postgres database (it will create the file if it doesn't exist)
engine = create_engine(os.environ["DATABASE_URL"])

# new changes
metadata = MetaData()

#define table columns
def create_columns(df):
    columns = [Column("id", Integer, primary_key=True, autoincrement=True)]
    for col_name in df.columns:
        if pd.api.types.is_integer_dtype(df[col_name]):
            columns.append(Column(col_name, BigInteger))
        elif pd.api.types.is_float_dtype(df[col_name]):
            columns.append(Column(col_name, SQLAlchemyFloat))
        else:
            columns.append(Column(col_name, VARCHAR(255)))
    return columns

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

columns = create_columns(df)
property = Table("property", metadata, *columns)
metadata.create_all(engine)
df.to_sql("property", engine, if_exists="append", index=False)

#return rows from newly property table to check if insertion happened successfully   
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) from property"))   
    count = result.fetchone()[0]
    print(f"number of records:{count}")

print("Data imported successfully!")
