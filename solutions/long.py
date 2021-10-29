"""
Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.
By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
"""

from Bio import SeqIO

# FILE="data/rosalind_long5.txt"
FILE="test_data/long2.fasta"

records = list(SeqIO.parse(FILE, "fasta"))
l = [record.seq for record in records]


def glue(s, t):
    """
    s                   -> str
    t                   -> str
    returns superstring -> str or None

    This function returns the superstring of two strings if there exists one. Otherwise returns None.
    Step 1: sort s and t by length
    Step 2: If t in s or s is equal to t return s.
    Step 3: Compare strings, starting from the first non-overlapping position:
    pos = len(s1) - (len(s2) - 1), with overlap of len(s2) - 1
    AAAGCT
      AGTTT
    
    Step 4: Compare strings, starting from the first non-overlapping position, but in the beginning:
     AAAGCT
    AGTTT
    Step 5: return superstring or None

    """ 
    # step 1
    if len(s) >= len(t):
        s1 = s 
        s2 = t
    else:
        s1 = t
        s2 = s 
    
    # step 2
    # if s1 == s2 or s2 in s1:
    #     return s1

    # step 3
    start = len(s1) - len(s2) - 1
    end = len(s1) - len(s2) // 2 + 1

    for pos in range(start, end):
        part1 = s1[pos:]
        part2 = s2[:len(part1)]

        if part1 == part2:
            # step 4
            return s1[:pos] + s2
    
    # step 4
    start = 1
    end = len(s2) // 2

    for pos in range(start, end):
        part1 = s2[pos:]
        part2 = s1[:len(part1)]

        if part1 == part2:
            return s2 + s1[pos:]

    # step 5
    return None
    

# new approach!
def assemble(reads):
    contig = reads[0]

    while len(reads) > 1:
        for read in reads:
            superstring = glue(contig, read)
            if superstring is not None:
                contig = superstring
                reads.remove(read)

    return(contig)

print(assemble(l))



