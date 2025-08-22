"""
Counting Point Mutations

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)

"""

def hamm_dist(s, t):
    score = 0
    for a, b in zip(s, t):
        if a!=b:
            score = score+1
    return score

#example
#s = "GAGCCTACTAACGGGAT"
#t = "CATCGTAATGACGGCCT"
#hamm_dist(s,t)
#7