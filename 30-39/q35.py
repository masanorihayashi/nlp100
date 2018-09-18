#encoding:utf-8

import MeCab

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
list_noun = []
for line in lines:
        nouns = []
        for i in line:
            if (i['pos'] == '名詞') :
                nouns.append(i['surface'])

            else:
                list_noun.append((''.join(nouns)))
                nouns = []

        if len(nouns) > 1:
            list_noun.append("".join(nouns))

print(set(list_noun))

