#encoding:utf-8

#from collections import Counter

with open('hightemp.txt', 'r') as f:
    total = set()
    for i in f:
        col1 = i.split('\t')[0]
        #char = list(col1)
        total.add(col1)
    #以下でも可
    #total = set(i.split('\t'))[0] for i in f)


print(total)
