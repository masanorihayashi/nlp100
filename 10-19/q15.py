#encoding:utf-8

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--number','-n', type=int, required=True)
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

    for i in lines[-args.number:]:
        print(i, end="")
