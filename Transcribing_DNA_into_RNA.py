"""
Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
"""


def tx_DNA_RNA(sequence):
    return sequence.replace("T", "U")

