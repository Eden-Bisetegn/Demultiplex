#!/usr/bin/env python
import bioinfo
import argparse
import gzip
import math

def get_args():
    parser = argparse.ArgumentParser(description="open four programs simultaneously")
    parser.add_argument("-f1", "--filename1", type=str, help="firstfilename", required=True)
    parser.add_argument("-f2", "--filename2", type=str, help="secondfilename")
    parser.add_argument("-f3", "--filename3", type=str, help="thiredfilename")
    parser.add_argument("-f4", "--filename4", type=str, help="fourthfilenme")
    return parser.parse_args()

args=get_args()
file1= args.filename1
file2=args.filename2
file3=args.filename3
file4=args.filename4


def rev_complement(seq):
    complement = {'A': 'T', 'a': 'T', 'C': 'G', 'c': 'G', 'G': 'C', 'g': 'C', 'T': 'A', 't': 'A', 'N': 'N', 'n': 'N'} 
    rev_com=""
    for base in seq:
        rev_com+=complement[base]
    return rev_com[::-1]

index_file="/projects/bgmp/shared/2017_sequencing/indexes.txt"

with open(index_file, "r") as fh:
    indexes=[]
    i=0
    for line in fh:
        i+=1
        line=line.strip()
        if i>1:
            indexes.append(line.split("\t")[4])

index_dict={}
for i in indexes:
    fh1=open(i+"_R1.fq", "w")
    fh2=open(i+"_R2.fq", "w")
    index_dict[i]=[fh1,fh2]

unk1= open("unknown_R1.fq","w")
unk2= open("unknown_R2.fq", "w")
hopped1=open("hopped_R1.fq", "w")
hopped2=open("hopped_R2.fq", "w")


R1rec=["","","",""]
R2rec=["","","",""]
R3rec=["","","",""]
R4rec=["","","",""]

matched={}
hopped={}

with gzip.open(file1, "rt") as r1, gzip.open(file2, "rt") as i1, gzip.open(file3,"rt") as i2, gzip.open(file4, "rt") as r2:
    total_num=0
    unk_num=0
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
        total_num+=1
        index1=R2rec[1].upper()
        index2=rev_complement(R3rec[1].upper())
        old_header1=R1rec[0]
        old_header2=R4rec[0]
        new_header1=old_header1+" "+index1+"-"+index2
        new_header2=old_header2+" "+index1+"-"+index2
        if "N" in index1 or "N" in index2:
            unk1.write(new_header1+"\n"+ R1rec[1]+"\n"+R1rec[2]+"\n"+R1rec[3]+"\n")
            unk2.write(new_header2+"\n"+ R4rec[1]+"\n"+R4rec[2]+"\n"+R4rec[3]+"\n")
            unk_num+=1
        elif  index1 not in indexes or index2 not in indexes:
            unk1.write(new_header1+"\n"+ R1rec[1]+"\n"+R1rec[2]+"\n"+R1rec[3]+"\n")
            unk2.write(new_header2+"\n"+ R4rec[1]+"\n"+R4rec[2]+"\n"+R4rec[3]+"\n")
            unk_num+=1
        elif index1!=index2:
            hopped1.write(new_header1+"\n"+ R1rec[1]+"\n"+R1rec[2]+"\n"+R1rec[3]+"\n")
            hopped2.write(new_header2+"\n"+ R4rec[1]+"\n"+R4rec[2]+"\n"+R4rec[3]+"\n")
            if index1+"-"+index2 in hopped:
                hopped[index1+"-"+index2]+=1
            else:
                hopped[index1+"-"+index2]=1
        elif index1==index2:
            index_dict[index1][0].write(new_header1+"\n"+ R1rec[1]+"\n"+R1rec[2]+"\n"+R1rec[3]+"\n")
            index_dict[index2][1].write(new_header2+"\n"+ R4rec[1]+"\n"+R4rec[2]+"\n"+R4rec[3]+"\n")
            if index1 in matched:
                matched[index1]+=1
            else:
                matched[index1]=1
        else:
            print("immpossible")

    R1rec=["","","",""]
    R2rec=["","","",""]
    R3rec=["","","",""]
    R4rec=["","","",""]

with open("matched_p.txt", "w") as fh:
    fh.write(f'Index\tnumberofmatchedpairs\tmatchedpercentage\tmatchedpersample\n')
    for key,value in matched.items():
        matched_perc=value/total_num*100
        tot_matched_perc=(sum(matched.values())/total_num)*100
        fh.write(f'{key}\t{value}\t{matched_perc}%\t{tot_matched_perc}%\n')

with open("hopped_p.txt", "w") as fh:
    fh.write(f'Index\tnumber of hopped pairs\thopped percentage\thoppedpersample\n')
    for key, value in hopped.items():
        hopped_perc=value/total_num*100
        tot_hopped_perc=(sum(hopped.values())/total_num)*100
        fh.write(f'{key}\t{value}\t{hopped_perc}%\t{tot_hopped_perc}%\n')

with open("unknown_t", "w")as fh:
    fh.write(f'The amount of unknown readpairs {unk_num}')

with open("summary.txt", "w") as fh:
    fh.write(f'Index_hopped\t{tot_hopped_perc}%\nmatched\t{tot_matched_perc}%\nunknown\t{(unk_num/total_num)*100}%\n') 
