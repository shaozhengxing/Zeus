#-*-coding:utf-8-*-
import requests;
import json;

token = 'ac538ed5f752ae6ea2ef09dd68264af8886f801d';
host = 'https://api.github.com'

def filter_data(data):
    return dict(filter(lambda x: x[1] != None, data.items()))

def get(api_function):
    def wrapper(*args, **kwargs):
        params = api_function(*args, **kwargs)
        headers = {'Accept':'application/vnd.github.v3+json', 'Authorization':'token ' + token}
        response = requests.get(host + params['api'], data=filter_data(params['data']), headers=headers)
        return response.json()

    return wrapper

def post(api_function):
    def wrapper(*args, **kwargs):
        params = api_function(*args, **kwargs)
        headers = {'Accept':'application/vnd.github.v3+json', 'Authorization':'token ' + token}
        response = requests.post(host + params['api'], data=json.dumps(filter_data(params['data'])), headers=headers)
        return response.json()
    return wrapper

def patch(api_function):
    def wrapper(*args, **kwargs):
        params = api_function(*args, **kwargs)
        headers = {'Accept':'application/vnd.github.v3+json', 'Authorization':'token ' + token}
        response = requests.patch(host + params['api'], data=json.dumps(filter_data(params['data'])), headers=headers)
        if (response.text):
            return response.json()
        else:
            return response.status_code
    return wrapper

def delete(api_function):
    def wrapper(*args, **kwargs):
        params = api_function(*args, **kwargs)
        headers = {'Accept':'application/vnd.github.v3+json', 'Authorization':'token ' + token}
        response = requests.delete(host + params['api'], data=json.dumps(filter_data(params['data'])), headers=headers)
        if (response.text):
            return response.json()
        else:
            return response.status_code
    return wrapper
