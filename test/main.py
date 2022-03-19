#!/usr/bin/python3
from json import dumps as jdump
from dotenv import dotenv_values
import requests

DATA= {
    'product_description': "aprasymas",
    'model':  "modelis",
    'meta_title': "title",
    'language_id': "1",
    'description': "kappa",
    'name': "kappa"
}

if __name__ == "__main__":
    config = {
        **dotenv_values('.env.example'),
        **dotenv_values('.env')
    }
    res = requests.post(config['URL'], DATA)
    print(f'Status code: {res.status_code}')
    print(jdump(res.json(), indent=2))
