#encoding:utf-8

with open ('hightemp.txt', 'r') as f:
    for num, line in enumerate(f, 1):
        print(line.rstrip())
    print('total line ', num)
