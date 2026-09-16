def sequence_type(seq):
    if isinstance(seq, coral.DNA):
        material = 'dna'
    elif isinstance(seq, coral.RNA):
        material = 'rna'
    elif isinstance(seq, coral.Peptide):
        material = 'peptide'
    else:
        raise ValueError('Input was not a recognized coral.sequence object.')
    return material