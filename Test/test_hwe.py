
import sys
import os
import pytest
import math
# pylint: skip-file
sys.path.append(".")
DIR = os.path.dirname(__file__)

import PopGen.hardy_weinberg as hwe
from Test.Format.fasta_outputs import CUBILIN_OUTPUT, MULTI_ENTIRES_OUTPUT

class TestHWE:
    def test_empty_allele_freq(self):
        with pytest.raises(AttributeError, match=r"Expected at least 1 frequency. Received 0."):
            hwe.get_allele_freq()

    def test_single_known_pp_freq(self):
        assert \
            hwe.get_allele_freq(0.05) == \
            {'p': math.sqrt(0.05), 'q': 1 - math.sqrt(0.05)}

    def test_single_known_qq_freq(self):
        assert \
            hwe.get_allele_freq(None, 0.05) == \
            {'q': math.sqrt(0.05), 'p': 1 - math.sqrt(0.05)}

    def test_trivial_get_carrier_freq(self):
        assert hwe.get_carrier_freq(0) == 0.0
        assert hwe.get_carrier_freq(1) == 0.0

    def test_get_carrier_freq(self):
        assert hwe.get_carrier_freq(0.25) == 0.5

    