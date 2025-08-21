"""
#Computing GC Content
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

"""

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

def highest_gc(fasta_file):
    max_gc = -1
    max_id = ""

    for record in SeqIO.parse(fasta_file, "fasta"):
        gc = gc_fraction(record.seq)

        if gc > max_gc:
            max_gc = gc
            max_id = record.id
    return print(max_id, '\n', round(max_gc*100,2))


#example
#highest_gc("rosalind_gc.txt")