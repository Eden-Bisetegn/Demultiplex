#!/usr/bin/env python
import argparse
import gzip
import math

def get_args():
    parser = argparse.ArgumentParser(description="A program to introduce yourself")
    parser.add_argument("-f", "--name", help="Your file name", required=True)
    parser.add_argument("-o", "--output", help="output_filename", required=True)
    parser.add_argument("-n", "--figure_name", help="figure_name", required=True)
    parser.add_argument("-l", "--length", type=int, help="length_list", required=True)
    return parser.parse_args()

args=get_args()
filename= args.name
output=args.output
figure_name=args.figure_name
length=args.length

def convert_phred(letter: str) -> int:
    return ord(letter) - 33

def init_list(lst: list,length, value:float = 0.0) -> list:
    for i in range(length):
        lst.append(value)
    return lst
my_list: list = []
my_list = init_list(my_list,length)
#print("created a list that is", len(my_list), "long")
with gzip.open(filename, "rt")as fh:
# with open(filename, "r")as fh:
    i = 0   # to count the number of lines - starts at 0
    for line in fh:
        if i%4 == 3:
            line = line.strip('\n')
            for e, letter in enumerate(line):
                score=convert_phred(letter)
                my_list[e]+=score
        i+=1      # to count the numb
# print(my_list, i)

# def calc mean 
num_lines=len(filename) # should be "i" since that is the counter for the num_lines of the file passing through (num_lines=i)

for i, mean in enumerate(my_list):
    my_list[i]=my_list[i]/(num_lines/4)
    # print(i, my_list[i])


import matplotlib.pyplot as plt

plt.bar(range(length),my_list)

plt.xlabel("Nuclotide position")
plt.ylabel("Average quality score") 
plt.title("Pernuclotide mean distribution of Read1")

plt.savefig(figure_name)