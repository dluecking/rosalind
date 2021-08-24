"""
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""

from Bio import SeqIO

# FILE="data/rosalind_long.txt"
FILE="test_data/04_long.fasta"

records = list(SeqIO.parse(FILE, "fasta"))
l = [record.seq for record in records]

def glue(s, t):
    if s in t:
        return t
    if t in s:
        return s
    for i in range(len(s) // 2 + 1):
        j = 0
        while s[i+j] == t[j]:
            j += 1
            if i + j >= len(s) or j >= len(t):
                return(s[:i]+t)

def shrinkList(list_of_seqs):
    new_list = []
    for seq1 in list_of_seqs:
        for seq2 in list_of_seqs:
            if seq1 != seq2:
                super_string = glue(seq1, seq2)
                if super_string is not None:
                    print("seq1 = {} -- seq2 = {}".format(seq1, seq2))
                    print("superstring = {}".format(super_string))
                    new_list.append(super_string)
                    break
    return(list(set(new_list)))

def assemble2(list_of_seqs):
    while len(list_of_seqs) > 1:
        list_of_seqs = shrinkList(list_of_seqs)
    return(list_of_seqs[0])

    
print(assemble2(l))

