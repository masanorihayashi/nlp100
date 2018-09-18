#encoding:utf-8

import gzip
import json
import re

 
def uk():
    with gzip.open('jawiki-country.json.gz', 'rt') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    
    raise ValueError('not found')


data = uk()

pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^\}\}$', re.MULTILINE + re.DOTALL)

result = pattern.findall(data)

pattern2 = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern2.findall(data)

result = {}
for i in fields:
    result[i[0]] = i[1]

print(result['面積値'])
