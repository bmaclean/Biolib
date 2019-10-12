# pylint: skip-file
import sys
import os
import pytest

sys.path.append(".")
DIR = os.path.dirname(__file__)

import PopGen.hardy_weinberg as hwe
from Test.Format.fasta_outputs import CUBILIN_OUTPUT, MULTI_ENTIRES_OUTPUT

class TestHWE:
    def test_empty_allele_freq(self):
        with pytest.raises(AttributeError, match=r"Expected at least 1 frequency. Received 0."):
            hwe.get_allele_freq()
    
    