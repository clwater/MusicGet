# coding=utf-8


import hashlib
import json

import requests

def getMusic(id):
    url = 'http://music.163.com/#/song?id='
    url = url + str(id)
    musicHtml =  requests.get(url)
    print musicHtml.text

def searchMusicList(name):
    search_url = 'http://music.163.com/api/search/get'
    stype = 1
    offset = 0
    total = 'true'
    data = {
        's': name,
        'type': stype,
        'offset': offset,
        'total': total,
        'limit': 60
    }
    r = requests.post(search_url, data=data)
    # print r.text
    _data = json.loads(r.text)
    # print(_data['result']['songs'])
    _data = _data['result']['songs']

    # print _data[0]

    for _info in _data:
        print _info['id'] , _info['name']

    getMusic(482108711)

