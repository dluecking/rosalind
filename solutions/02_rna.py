"""
Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t
"""
import re

# FILE="test_data/02_rna.fasta"
FILE="data/rosalind_rna.txt"

f = open(FILE, "r")
t = f.read()
l = re.sub("T", "U", t)

print(l)


## without re
l2 = t.replace("T", "U")
print(l2)
