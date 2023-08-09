#!/usr/bin/env python
# import bioinfo
import argparse
import gzip
import math

# def get_args():
#     parser = argparse.ArgumentParser(description="A program to introduce yourself")
#     parser.add_argument("-f", "--name", help="Your file name", required=True)
#     parser.add_argument("-o", "--output", help="output_filename", required=True)
#     parser.add_argument("-n", "--figure_name", help="figure_name", required=True)
#     parser.add_argument("-l", "--length", type=int, help="length_list", required=True)
#     return parser.parse_args()

# args=get_args()
# filename= args.name
# output=args.output
# figure_name=args.figure_name
# length=args.length
#will import bioinfo so no need for definig each term 
# def reverse transcription  
#     ```Takes the sequence line and if its in the dictionary it returns the reverse transcriptome ```
#     return revese transcription
# create a dictionary = {}
# key - 4 diffrent bases 
# value - reverse transcriptome 
def ReverseComplement(file):
    revcomp = []
    x = len(file)
    for i in file:
        x = x - 1
        revcomp.append(file[x])
    return ''.join(revcomp)

# this if for the compliment 

def compliment(Nucleotide):
    comp = []
    for i in Nucleotide:
        if i == "T":
            comp.append("A")
        if i == "A":
            comp.append("T")
        if i == "G":
            comp.append("C")
        if i == "C":
            comp.append("G")

    return ''.join(comp)

# # def append the index to the header
#     ``` attaches the appropriate index to each read ```
#     return header with an index 
# input - header 
# out put - index-header 

R1rec=["","","",""]
R2rec=["","","",""]
R3rec=["","","",""]
R4rec=["","","",""]

file1= "/projects/bgmp/bisetegn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_testR1.txt"
file2= "/projects/bgmp/bisetegn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_testR2.txt"
file3= "/projects/bgmp/bisetegn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_testR3.txt"
file4= "/projects/bgmp/bisetegn/bioinfo/Bi622/Demultiplex/TEST-input_FASTQ/Unit_testR4.txt"

with (open(file1, "r")as r1, open(file2, "r") as i1, open(file3,"r") as i2, open(file4, "r") as r2):
    while True:
        R1rec[0]=r1.readline().strip()
        if R1rec[0] == "":
            break
        R1rec[1]=r1.readline().strip()
        R1rec[2]=r1.readline().strip()
        R1rec[3]=r1.readline().strip()
        
        R2rec[0]=i1.readline().strip()
        R2rec[1]=i1.readline().strip()
        R2rec[2]=i1.readline().strip()
        R2rec[3]=i1.readline().strip()
       
        R3rec[0]=i2.readline().strip()
        R3rec[1]=i2.readline().strip()
        R3rec[2]=i2.readline().strip()
        R3rec[3]=i2.readline().strip()
       
        R4rec[0]=r2.readline().strip()
        R4rec[1]=r2.readline().strip()
        R4rec[2]=r2.readline().strip()
        R4rec[3]=r2.readline().strip()
        
        # print(R1rec)
        # print(R2rec)
        # print(R3rec)
        # print(R4rec)
        
        R1rec=["","","",""]
        R2rec=["","","",""]
        R3rec=["","","",""]
        R4rec=["","","",""]

index_file="/projects/bgmp/shared/2017_sequencing/indexes.txt"

with open(index_file, "r") as fh:
    indexes=[]
    i=0
    for line in fh:
        i+=1
        line=line.strip()
        if i>1:
            indexes.append(line.split("\t")[4])
# print(indexes)
# print(len(indexes))

index_dict={}
for i in indexes:
    fh1=open(i+"_R1.fq", "w")
    fh2=open(i+"_R2.fq", "w")
    index_dict[i]=[fh1,fh2]
print(index_dict)

unk1= open("unknown_R1.fq","w")
unk2= open("unknown_R2.fq", "w")
hopped1=open("hopped_R1.fq", "w")
hopped2=open("hopped_R2.fq", "w")
