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

pattern = re.compile(r'\[\[Category:(.*?)(?:\|.*)?\]\]', re.MULTILINE)

result = pattern.findall(data)

for i in result:
    print(i)
