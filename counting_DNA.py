"""

Given: A DNA string s
 of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
"""

def count_nc(sequence):
    return sequence.count("A"), sequence.count("C"), sequence.count("G"), sequence.count("T")