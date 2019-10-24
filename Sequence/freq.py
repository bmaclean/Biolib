"""
get_component_frequency provides the frequency of a given sequence element within
the provided sequence.

Would commonly be used to determine base pair frequency in nucleic acid sequences, or
amino acid frequency in peptide sequences.

Example using partial application:

from functools import partial

tyr_freq = partial(freq, component='Y')
print(tyr_freq('TWWBCYCY')) # 0.25
"""

def get_component_frequency(component, seq):
    """Returns the frequency of `component` in `sequence`."""
    count = 0
    for elem in seq:
        if elem is component:
            count += 1
    return count / len(seq)
