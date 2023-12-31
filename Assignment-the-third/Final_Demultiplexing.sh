#!/bin/bash
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=bisetegn@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=1                 #optional: number of cpus, default is 1
#SBATCH --mem=32GB                        #optional: amount of memory, default is 4GB
#can find files to upload in the directory mentioned on slack
#SBATCH --error=demultiplex_%j.err                        #reqired: error account
#SBATCH --out=demultiplex_%j.out                        #reqired: output account
conda activate base 

/usr/bin/time -v ./Final_Demultiplexing.py \
    -f1 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz \
    -f2 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz \
    -f3 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz \
    -f4 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz