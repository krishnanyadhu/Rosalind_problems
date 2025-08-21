"""
#Complementing a Strand of DNA
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

"""
def rev_comp(sequence):
    complements = str.maketrans("ATCG", "TAGC")
    return sequence[::-1].translate(complements)

rev_comp(sequence)