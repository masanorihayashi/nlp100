#encoding:utf-8

from collections import Counter

with open('hightemp.txt', 'r') as f:
    result = []
    for i in f:
        result.append(i.split('\t')[0])

for k, v in sorted(Counter(result).items(), key=lambda x:x[1], reverse=True):
    print(k, v)

