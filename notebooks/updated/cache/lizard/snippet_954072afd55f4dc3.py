def calibrate_percentile_ranks(self, peptides=None, num_peptides_per_length
    =int(100000.0), alleles=None, bins=None):
    if bins is None:
        bins = to_ic50(numpy.linspace(1, 0, 1000))
    if alleles is None:
        alleles = self.supported_alleles
    if peptides is None:
        peptides = []
        lengths = range(self.supported_peptide_lengths[0], self.
            supported_peptide_lengths[1] + 1)
        for length in lengths:
            peptides.extend(random_peptides(num_peptides_per_length, length))
    encoded_peptides = EncodableSequences.create(peptides)
    for i, allele in enumerate(alleles):
        predictions = self.predict(encoded_peptides, allele=allele)
        transform = PercentRankTransform()
        transform.fit(predictions, bins=bins)
        self.allele_to_percent_rank_transform[allele] = transform
    return encoded_peptides