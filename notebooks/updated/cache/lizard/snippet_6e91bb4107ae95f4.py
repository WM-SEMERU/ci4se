def _validate_fasta_vs_seqres(self):
    pdb_id = self.pdb_id
    for chain_id, sequence in self.pdb.seqres_sequences.iteritems():
        if str(sequence) != self.FASTA[pdb_id][chain_id]:
            if self.pdb_id in use_seqres_sequence_for_fasta_sequence:
                self.FASTA.replace_sequence(self.pdb_id, chain_id, str(
                    sequence))
            elif self.pdb_id in use_fasta_sequence_for_seqres_sequence:
                self.pdb.seqres_sequences[chain_id] = Sequence.from_sequence(
                    chain_id, self.FASTA[pdb_id][chain_id], self.
                    sequence_types[chain_id])
                sequence = self.FASTA[pdb_id][chain_id]
            if str(sequence) != self.FASTA[pdb_id][chain_id]:
                raise colortext.Exception(
                    'The SEQRES and FASTA sequences disagree for chain %s in %s. This can happen but special-case handling (use_seqres_sequence_for_fasta_sequence) should be added to the file containing the %s class.'
                     % (chain_id, pdb_id, self.__class__.__name__))