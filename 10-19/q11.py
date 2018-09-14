#encoding:utf-8

with open ('hightemp.txt', 'r') as f:
    for i in f:
        print(i.replace('\t', ' '), end='')

