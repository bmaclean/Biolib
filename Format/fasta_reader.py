fasta_input = open('./cubilin.fasta')
fasta_output = open('./cubilin.txt')

aa_sequence = ''
header = ''

with fasta_input as file:
    for line in file:
        if line[0] == '>':
            header = line
        else:
            aa_sequence += line






