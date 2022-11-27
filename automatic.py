from humai_desarrollo_1 import my_etl as etl
from random import randint

number = randint(0, 500)


def main(number):
    """Se elige un número al azar y te devuelve un texto asociado"""
    number, data = etl.number_api_extract(number)
    print(data)
    df = etl.load(number, data)
    etl.transform(df)


if __name__ == "__main__":
    main(number)
