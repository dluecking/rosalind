"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
"""

from Bio import SeqIO

FILE = "data/rosalind_gc.txt"
# FILE = "test_data/06_gc.fasta"

records = list(SeqIO.parse(FILE, "fasta"))


max_gc = 0
max_gc_accesion = 0

for record in records:
    seq = record.seq.lower()
    gc_count = 0

    for char in seq:
        if char == "g" or char == "c":
            gc_count += 1
        gc_content = gc_count/len(seq)*100

    if gc_content > max_gc:
        max_gc = gc_content
        max_gc_accesion = record.id

print(max_gc_accesion)
print(max_gc)