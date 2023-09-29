"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests
import os
import io
import zipfile


def extract(
    url="https://github.com/johncoogan53/sqlite-lab_John-Coogan/raw/main/game_sales_data.csv",
    file_path="data/game_data.csv",
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
