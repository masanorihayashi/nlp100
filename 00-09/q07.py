#encoding:utf-8

def sentence_template(x, y, z):
    #return '{hour}時の{words}は{value}'.format(hour=x, words=y, value=z)
    #モダンな書き方？
    return f'{x}時の{y}は{z}'

print(sentence_template(12, '気温', 22.4))
