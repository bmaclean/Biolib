import Bio
from Bio import SeqIO

fasta_input = '/cubilin.fasta'

fasta_sequences = SeqIO.parse(open(fasta_input),'fasta')

