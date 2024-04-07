import requests
import json


def json_data(date):
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://127.0.0.1',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    print(date)
    print(requests.post("http://127.0.0.1/dev-api/login", data=json.dumps(date), headers=head).json())
