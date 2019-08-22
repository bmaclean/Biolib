# pylint: skip-file

import sys
import os

sys.path.append(".")
DIR = os.path.dirname(__file__)

import pytest

import Format.fasta as fasta

class TestFasta:
    def test_empty_input(self):
        file_path = os.path.join(DIR, './Format/empty.fasta')
        empty_file = open(file_path)
        assert fasta.from_fasta(empty_file) == []

    def test_invalid_file_input(self):
        with pytest.raises(AttributeError):
            assert fasta.from_fasta('')
            assert fasta.from_fasta('./Format/cubilin.fasta')
            
