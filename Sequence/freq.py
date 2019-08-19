"""
`freq` provides the frequency of a given sequence element within the provided sequence.

Would commonly be used to determine base pair frequency in nucleic acid sequences, or
amino acid frequency in peptide sequences.

Example using partial application:

from functools import partial

tyr_freq = partial(freq, component='Y')
print(tyr_freq('TWWBCYCY')) # 0.25
"""

def freq(component, seq=[]):
    count = 0
    for a in seq:
        if a is component:
            count += 1
    return count / len(seq)