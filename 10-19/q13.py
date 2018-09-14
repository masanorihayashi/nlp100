#encoding:utf-8


with open ('col1.txt', 'r') as f1 , open('col2.txt', 'r') as f2, open('reconcat.txt', 'w') as fw:
    for i, j in zip(f1, f2):
        fw.write(i.rstrip() + '\t' + j.rstrip() + '\n')
        
