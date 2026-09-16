def protein_sequence(self, protein_id):
    if self.protein_sequences is None:
        raise ValueError('No protein FASTA supplied to this Genome: %s' % self)
    return self.protein_sequences.get(protein_id)