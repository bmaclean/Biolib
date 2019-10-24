"""
    hardy_weinberg contains functions for modelling a population in
    Hardy-Weinberg equilibrium and determining allele frequencies given
    genotypic frequency.
"""
import math

def get_allele_freq(pp_freq=None, qq_freq=None):
    """
        Receives the genotypic frequency of either pp or qq, and returns the allele
        frequencies of alleles p and q.
    """
    if pp_freq is None and qq_freq is None:
        raise AttributeError("Expected at least 1 frequency. Received 0.")
    elif pp_freq is not None and qq_freq is not None:
        # both genotype frequencies provided
        return {
            'p': math.sqrt(pp_freq),
            'q': math.sqrt(qq_freq)
        }
    elif qq_freq is None:
        # pp genotype frequency provided
        return {
            'p': math.sqrt(pp_freq),
            'q': 1 - math.sqrt(pp_freq)
        }
    else:
        # qq genotype frequency provided
        return {
            'p': 1 - math.sqrt(qq_freq),
            'q': math.sqrt(qq_freq)
        }

def get_carrier_freq(f_homo):
    """
        Given either homozygous frequency, returns the heterozygous frequency.
    """
    return 2 * (math.sqrt(f_homo) * (1 - math.sqrt(f_homo)))

def in_hwe(gen_1, gen_2):
    """
        Given the allele frequenceis of two generations 1 and 2, returns True if that
        population is in Hardy-Weinberg equilibrium between those generations.

        gen_1 and gen_2 are of the format:
        {
            p: 0.7,
            q: 0.3
        }

        Where p and q are alleles in the gene pool.

        A `False` result from is_hwe suggests the given gene is not undergoing evolution.
    """
    return gen_1.p == gen_2.p and gen_1.q == gen_2.q
