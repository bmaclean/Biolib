"""
    Fasta is a collection of functions for FASTA file format I/O.
"""

def from_fasta(fasta_file):
    """Returns an array of dicts for each record in a given FASTA file."""
    records = []
    record_index = 0
    with fasta_file as file:
        for line in file:
            if line[0] == '>':
                records.append(dict())
                records[record_index]['header'] = line.rstrip("\n\r")
                records[record_index - 1]['sequence'] = ''
                record_index += 1
            else:
                records[record_index - 1]['sequence'] += line.rstrip("\n\r")
    print(records)
    return records

def to_fasta(source, target):
    """Writes a given data structure to FASTA file format at `target`."""
    return source
