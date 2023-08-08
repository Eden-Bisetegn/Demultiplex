# Author: Eden Bisetegn <bissetegn@uoregon.edu>

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.1"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = None
RNA_bases = None

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter) - 33

def qual_score(phred_score: str) -> float:
    '''Write your own doc string'''
phred_score=[]
qual_score=0
i=1
for value in (phred_score):
    score=convert_phred(value)
    qual_score=score+qual_score
    i+=1

def validate_base_seq():
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    sequence=sequence.upper() # turnes all the sequences to upper case letters 
    valid_base=set('ACTG')
    for i in sequence:
        if i not in valid_base:
            return False
        else:
            return True

def gc_content(DNA):
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    gc_content = DNA.count('G') + DNA.count('C')
    return gc_content/len(DNA)

def oneline_fasta(output: str, filename: str):
    '''docstring'''
    sequence: str=''
    header: str=''
    with open(output, "w") as reads, open(filename, "r") as fh:
        for line in fh:
            line=line.strip("\n")
            if line.startswith('>'):
                if sequence=='':
                    header=line
                else:
                    reads.write(f'{header}\n{sequence}\n')
                    sequence=''
                    header=line
            else:
                sequence+=line
        reads.write(header)
        reads.write(sequence)

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

if __name__ == "__main__":
    assert validate_base_seq("AATAGAT", False) == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    assert validate_base_seq("TATUC",False) == False
    assert validate_base_seq("UCUGCU", False) == False
    print("Passed DNA and RNA tests")

if __name__ == "__main__":
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("correctly calculated GC content")

# if __name__ == "__main__":
#     assert oneline_fasta(f'{header}\n{sequence}') == True 
#     print("correctly made oneline fasta")
    