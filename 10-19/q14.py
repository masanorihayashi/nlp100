#encoding:utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--number','-n', type=int, required=True)
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
    for num, i in enumerate(f, 0):
        if num == args.number:
            break
        else:
            print(i.rstrip())
