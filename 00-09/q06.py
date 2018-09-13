#encoding:utf-8

str1 = "paraparaparadise"
str2 = "paragraph"

def ngram(strings, n):
    result = []
    for i in range(0, len(strings) -n + 1):
        result.append(strings[i:i + n])
    return result


X = set(ngram(str1, 2))
Y = set(ngram(str2, 2))

#和集合
print(X.union(Y))
#積集合
print(X.intersection(Y))
#差集合
print(X.difference(Y))

#冗長
'''
if 'se' in X:
    print(True)
else:
    print(False)

if 'se' in Y:
    print(True)
else:
    print(False)
'''
print(str('se' in X))
print(str('se' in Y))
