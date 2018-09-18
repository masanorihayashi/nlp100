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
no = []
for line in lines:
    if len(line) > 2: 
        for i in range(1, len(line) -1):
            if (line[i]['surface'] == 'の') \
                and (line[i-1]['pos'] == '名詞') \
                and (line[i+1]['pos'] == '名詞') :
                no.append(line[i-1]['surface'] + line[i]['surface'] + line[i+1]['surface'])

print(set(no))

