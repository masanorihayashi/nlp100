#encoding:utf-8

import gzip
import json
import re
import urllib.parse, urllib.request

 
def uk():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    
    raise ValueError('not found')


data = uk()

def rm_markup(lines):
    pattern = re.compile(r"(\'{2,5})(.*?)(\1)", re.MULTILINE)
    lines =  pattern.sub(r'\2', lines)
    pattern = re.compile(r"\[\[(?:[^|]*?\|)?([^|]*?i)\[\[", re.MULTILINE)
    lines = pattern.sub(r'\1', lines)
    pattern = re.compile(r"\{\{lang(?:[^|]*?\|)*?([^|]*?)\}\}", re.MULTILINE)
    lines = pattern.sub(r'\1', lines)
    pattern = re.compile(r"\[http:\/\/(?:[^\s]*?\s)?([^]]*?)\]", re.MULTILINE)
    lines = pattern.sub(r'\1', lines)
    pattern = re.compile(r"<\/?[br|ref][^>|]*?>", re.MULTILINE)
    lines = pattern.sub('', lines)


    return lines

pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.DOTALL)

result = pattern.findall(data)

pattern2 = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern2.findall(data)

result = {}
for i in fields:
    result[i[0]] = rm_markup(i[1])

name = result['国旗画像']
print(name)
url =  'https://www.mediawiki.org/w/api.php?' \
        + 'action=query' \
        + '&titles=File:' + urllib.parse.quote(name) \
        + '&format=json' \
        + '&prop=imageinfo' \
        + '&iiprop=url'

request = urllib.request.Request(url,
        headers={'User_agent': 'testuser'})
connection = urllib.request.urlopen(request)

out = json.loads(connection.read().decode())
print(out)

url = out['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)
