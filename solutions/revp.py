"""
A DNA string is a reverse palindrome if it is equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.
Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
"""
from Bio import SeqIO


FILE = "data/rosalind_revp.txt"
# FILE = "test_data/rosalind_revp.txt"

records = list(SeqIO.parse(FILE, "fasta"))
seq = records[0].seq 

palindrome_lengths = list(range(4, 13, 2)) # 4, 6, 8, 10, 12

for l in palindrome_lengths:
    for pos in range(0, len(seq)-l+1):
        site = seq[pos:pos+l]
        if site == site.reverse_complement():
            print(f"{pos+1} {l}")
