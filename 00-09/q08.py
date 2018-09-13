#encoding:utf-8

def cipher(strings):
    result = ''
    for i in strings:
        if i.islower():
            result += chr(219 - ord(i))
        else:
            result += i
    return result


target = input('plz enter strings-->> ')

#暗号化
result = cipher(target)
print('暗号化：', result)
#復号化
result = cipher(result)
print('復号化：', result)

