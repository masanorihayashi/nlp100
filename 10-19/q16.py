#encoding:utf-8

import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--number','-n', type=int, required=True)
args = parser.parse_args()


with open('hightemp.txt', 'r') as f:
    num_lines = sum(1 for line in f)
    split_num = math.ceil(num_lines/args.number)
    print(split_num)
    f.seek(0)
    total = 1
    for num, i in enumerate(f, 0):
        if num % split_num == 0:
            print(f'==========={total}==========')
            print(i,end='')
            total += 1
        else:
            print(i, end='')
