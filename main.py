"""
ETL-Query script
"""
import fire
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query


def main(query_string):
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query
    print("Querying data...")
    query(query_string)


if __name__ == "__main__":
    fire.Fire(main)
