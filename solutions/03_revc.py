"""
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

s = input()
s = s.lower()
sr = s[::-1]
for x, y in zip(["a", "c", "t", "g"], ["T", "G", "A", "C"]):
    sr = sr.replace(x, y)
print(sr)
