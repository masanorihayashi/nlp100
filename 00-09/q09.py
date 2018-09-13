#encoding:utf-8

import random


def replacement(strings):
    result = []
    for i in strings.split():
        if len(i) <= 4:
            result.append(i)
        else:
            randlist  =[]
            char = list(i)
            randlist.append(char[0])
            randlist.append(''.join(random.sample(char[1:-1], len(char)-2)))
            randlist.append(char[-1])
            result.append(''.join(randlist))

    return ' '.join(result)


strings = input('plz input strings -->> ') 
print(replacement(strings))

