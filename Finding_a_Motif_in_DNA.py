"""
Finding a Motif in DNA
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

def locations(seq1, seq2):
    loc = []
    for i in range(len(seq1)):
        if seq2 == seq1[i:i+len(seq2)]:
            loc.append(i+1)
    return loc

f= open("rosalind_subs.txt", "r")
seq1 = f.readline().strip()
seq2 = f.readline().strip()

result = locations(seq1, seq2)
for i in result:
    print(i, end=" ")
