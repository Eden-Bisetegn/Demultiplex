# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | read1 | 101 | Phred33+ |
| 1294_S1_L008_R2_001.fastq.gz | index1 | 8 | Phred33+ |
| 1294_S1_L008_R3_001.fastq.gz | index2 | 8 | Phred33+ |
| 1294_S1_L008_R4_001.fastq.gz | read2 | 101 | Phred33+ |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. For both index and biological read I chose a min of phred 30 (1 in 1000). Since index reads are used to identify which sample belongs to which read we should have a higher expectation of quality to lower the chance of misidentifying samples. As for the biological reads, we would need a high-quality score to get a more accurate base call.
       
    4. **YOUR ANSWER HERE**
    
## Part 2
1. Define the problem
2. Describe output
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
