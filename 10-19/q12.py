#encoding:utf-8

'''
with open ('hightemp.txt', 'r') as f:
    col1 = []
    col2 = []
    for line in f:
        one, two = line.split('\t')[0], line.split('\t')[1]
        col1.append(one)
        col2.append(two)

    with open('col1.txt', 'w') as f1:
        for i in col1:
            f1.write(i)
            f1.write('\n')

    with open('col2.txt', 'w') as f2:
        for i in col2:
            f2.write(i)
            f2.write('\n')
'''
with open ('hightemp.txt', 'r') as f, open('col1.txt', 'w') as f1, open('col2.txt', 'w') as f2:
    col1 = []
    col2 = []
    for line in f:
        one, two = line.split('\t')[0], line.split('\t')[1]
        f1.write(one + "\n")
        f2.write(two + "\n")
