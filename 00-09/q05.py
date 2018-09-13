#encoding:utf-8

sentence = "I am an NLPer"

def ngram(list, n):
    result = []
    for i in range(0, len(list) -n + 1):
        result.append(list[i:i +n])
    return result


words = sentence.split()
word_bigram = ngram(words, 2)
print(word_bigram)

char_bigram = ngram(sentence, 2)
print(char_bigram)
