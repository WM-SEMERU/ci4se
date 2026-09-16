def _guess_sequence_type_from_string(self, seq):
    aa_chars = ['P', 'V', 'L', 'I', 'M', 'F', 'Y', 'W', 'H', 'K', 'R', 'Q',
        'N', 'E', 'D', 'S', 'X', '*']
    aas = set(itertools.chain(aa_chars, [lower(a) for a in aa_chars]))
    na_chars = ['A', 'T', 'G', 'C', 'N', 'U']
    nas = set(itertools.chain(na_chars, [lower(a) for a in na_chars]))
    num_nucleotide = 0
    num_protein = 0
    count = 0
    for residue in seq:
        if residue in nas:
            num_nucleotide += 1
        elif residue in aas:
            num_protein += 1
        else:
            raise Exception(
                'Encountered unexpected character when attempting to guess sequence type: %s'
                 % residue)
        count += 1
        if count > 300:
            break
    if float(num_protein) / (num_protein + num_nucleotide) > 0.1:
        return self.PROTEIN_SEQUENCE_TYPE
    else:
        return self.NUCLEOTIDE_SEQUENCE_TYPE