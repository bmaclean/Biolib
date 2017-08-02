import amino_acid
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

tyr_count = 0
aa_count = 0
for a in aa_sequence:
    if a is amino_acid.AminoAcid.tyr.abbrv:
        tyr_count += 1
    aa_count += 1

print('Tyrosine frequency: ' + str(tyr_count/aa_count))





