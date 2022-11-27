import requests


def number_api(number):
    # el endpoint de la API
    key = f"http://numbersapi.com/{number}"
    data = requests.get(key)
    data = data.text
    return data
