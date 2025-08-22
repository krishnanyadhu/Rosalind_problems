"""
Translating RNA into Protein
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s

"""

#without biopython

def translate(seq):
    codon_table = {
        'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
    'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
    'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop',
    'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
    'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
    'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
    'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
    'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
    'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
    'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
    'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
    }
    protein = ''
    for i in range(0, len(seq), 3):
        amino_acid = codon_table[seq[i:i+3]]
        if amino_acid == "Stop":
            break
        protein += amino_acid
    return protein

#example
#translate("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

#with biopython

from Bio.Seq import Seq
rna = Seq("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")
protein = rna.translate(to_stop=True)
print(protein)
