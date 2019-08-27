"""
    hardy_weinberg contains functions for calculating if a population is in
    Hardy-Weinberg equilibrium, and allele frequencies given phenotype frequency.
"""
import math

def get_allele_freq(pp_freq=None, qq_freq=None):
    """
        Receives the phenotypic frequency of either pp or qq, and returns the allele
        frequencies of p and q.
    """
    if pp_freq is None and qq_freq is None:
        raise Exception
    if qq_freq is None:
        # pp phenotype frequency provided
        return {
            'p': math.sqrt(pp_freq),
            'q': 1 - math.sqrt(pp_freq)
        }
    else:
        # qq phenotype frequency provided
        return {
            'p': 1 - math.sqrt(qq_freq),
            'q': math.sqrt(qq_freq)
        }
