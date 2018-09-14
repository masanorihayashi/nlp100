#encoding:utf-8

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()
    lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for i in lines:
    print(i, end='')
