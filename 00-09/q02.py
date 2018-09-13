#encoding:utf-8

char1 = 'パトカー'
char2 = 'タクシー'
concat = ''

for i,j in zip(list(char1), list(char2)):
    concat += i + j

print(concat)
