def random_peptides(num, length=9, distribution=None):
    if num == 0:
        return []
    if distribution is None:
        distribution = pandas.Series(1, index=sorted(amino_acid.
            COMMON_AMINO_ACIDS))
        distribution /= distribution.sum()
    return [''.join(peptide_sequence) for peptide_sequence in numpy.random.
        choice(distribution.index, p=distribution.values, size=(int(num),
        int(length)))]