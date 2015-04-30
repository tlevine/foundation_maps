import json

def cookie(response):
    return response.headers['set-cookie'].partition(';')[0]

def getList(response):
    return response.json()
