# pylint: skip-file
import sys
import os
import pytest

sys.path.append(".")
DIR = os.path.dirname(__file__)

import Format.fasta as fasta
from Test.Format.fasta_outputs import CUBILIN_OUTPUT, MULTI_ENTIRES_OUTPUT

class TestFasta:
    def test_empty_input(self):
        file_path = os.path.join(DIR, './Format/empty.fasta')
        empty_file = open(file_path)
        assert fasta.from_fasta(empty_file) == []

    def test_invalid_file_input(self):
        with pytest.raises(AttributeError):
            assert fasta.from_fasta('')
            assert fasta.from_fasta('./Format/cubilin.fasta')
        
    def test_single_record(self):
        cubilin_fasta = open('Test/Format/cubilin.fasta')
        assert fasta.from_fasta(cubilin_fasta) == CUBILIN_OUTPUT
        
    def test_multiple_records(self):
        mutli_fasta = open('Test/Format/multi_entries.fasta')
        assert fasta.from_fasta(mutli_fasta) == MULTI_ENTIRES_OUTPUT
            
