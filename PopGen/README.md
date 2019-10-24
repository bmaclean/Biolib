# PopGen Package

## hardy_weinberg

*`hardy_weinberg`* provides a set of utilities related to the Hardy-Weinberg model used to analyze whether a population is undergoing changes in allele frequencies. It current contains three functions to represent this model:

#### *`get_allele_freq(pp, qq)`*

Given allele frequencies for either (or both) homozygous genotypes, returns the allele frequencies for `p` and `q`. In the form:

    ```python
    {
        p: 0.50,
        q: 0.50
    }
    ```

#### *`get_carrier_freq(f_homo)`*

Given either homozygous frequency, returns the heterozygous "carrier" frequency for a population in Hardy-Weinberg equilibrium.

#### *`in_hwe(gen_1, gen_2)`*

Given two allele frequencies from the same generation sampled at different times, `in_hwe` returns `True` if the population is in Hardy-Weinberg equilibrium. A `False` result implies that evolution has occurred at the given locus.



## TODO's

- Selection changes in allele frequencies
