# pylint: skip-file
import sys
import os
import pytest
import math
from functools import partial

sys.path.append(".")
DIR = os.path.dirname(__file__)

import Sequence.freq as freq

class TestFreq:
    def test_empty_sequence(self):
        assert freq.get_component_frequency([], 'A') == 0.00

    def test_with_partial_application(self):
        tyr_freq = partial(freq.get_component_frequency, component='Y')
        assert tyr_freq(seq = 'TWWBCYCY') == 0.25
    