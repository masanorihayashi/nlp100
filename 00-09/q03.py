#encoding:utf-8

from collections import Counter

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentence = sentence.replace(',','').replace('.', '')

charlist = []
for i in sentence.split():
    charlist.append(len(i))

print(charlist)
