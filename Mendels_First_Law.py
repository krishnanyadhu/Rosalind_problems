"""
Mendel's First Law
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k
 individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

def iprb(k, m, n):
    num = 4*n*(n-1) + 4*m*n + m*(m-1)
    den = 4*(k+m+n)*(k+m+n-1)
    prob_res = num/den
    return 1 - prob_res

f = open("rosalind_iprb.txt", "r")
k,m,n = map(int, f.readline().split(" "))
print(k,m,n)
iprb(k,m,n)