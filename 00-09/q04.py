#encoding:utf-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

num_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dic = {}

#enumerate(hoge, n)で開始数字を指定できる
for num, i in enumerate(sentence.split(), 1):
    if num in num_list:
        dic[i[0:1]] = num
    else:
        dic[i[0:2]] = num

print(dic)
