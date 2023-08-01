#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=bisetegn@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=4                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB
#can find files to upload in the directory mentioned on slack
#SBATCH --error=Demultiplex-g%j.err                        #reqired: error account
#SBATCH --out=Demultiplex-g%j.out                        #reqired: output account

/usr/bin/time -v ./Part_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -o Read1.txt -l 101 -n Read1.png

# /usr/bin/time -v ./Part_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -o Read4.txt -l 101 -n Read4.png

# /usr/bin/time -v ./Part_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -o Read2.txt -l 8 -n Read2.png

# /usr/bin/time -v ./Part_1.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -o Read3.txt -l 8 -n Read3.png