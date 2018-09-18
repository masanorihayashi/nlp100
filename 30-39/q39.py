#encoding:utf-8

import MeCab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from collections import Counter
import numpy as np

parsed = 'neko.txt.mecab'


def parse_per_sentence():
    with open(parsed, 'r') as f:

        morphemes = []
        for line in f:
            col = line.split('\t')
            if (len(col) < 2):
                pass
            else:
                res_cols = col[1].split(',')



            morpheme = {
                    'surface': col[0],
                    'base': res_cols[6],
                    'pos': res_cols[0],
                    'pos1': res_cols[1],
                    }

            morphemes.append(morpheme)

            if res_cols[1] == '句点':
                yield morphemes
                morphemes = []

parse_per_sentence()

lines = parse_per_sentence()
words = Counter()
for line in lines:
    for i in line:
        if i['pos'] == '記号':
            pass
        else:
            words.update(i['surface'])

freq = []
list_zipped = list(zip(*words.most_common()))

#print(list_zipped)
words = list_zipped[0]
freq = list_zipped[1]

freqs = sorted(set(freq), reverse=True)
ranks = [i for i in range(1, len(set(freq))+1)]
print(ranks)

flog = np.log(np.array(freqs))
rlog = np.log(np.array(ranks))

plt.scatter(flog, rlog)
plt.show()
