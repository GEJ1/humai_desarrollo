import requests
import pandas as pd
from datetime import datetime
import os
from typing import Tuple

DATA_PATH = "/data"


def number_api_extract(number: int) -> Tuple[int, str]:
    """Calls numbers

    Args:
        number (int): The chosen number

    Returns:
        Tuple[int, str]: Number choosed and string with the asociated text
    """
    key = f"http://numbersapi.com/{number}"
    data = requests.get(key)
    data = data.text
    return number, data


def load(number: int, data: str) -> pd.DataFrame:
    """Load data into Pandas DataFrame

    Args:
        number (int): The chosen number
        data (str): Text for the number

    Returns:
        pd.DataFrame: ALl the info together in a DataFrame structure.
    """
    df = pd.DataFrame({"number": number, "data": [data]}, columns=["number", "data"])
    return df


def transform(df: pd.DataFrame) -> None:
    """Get the DataFrame and save into csv with datetime info as a name

    Args:
        df (pd.DataFrame): _description_
    """
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y-%H-%M-%S")
    actual_dir = os.getcwd()
    dir = actual_dir + "/" + DATA_PATH
    if not os.path.exists(dir):
        os.mkdir(dir)

    df.to_csv(dir + "/" + date_time, index=False)
