def _add_sequence(self, pdbID, chainID, sequence):
    pdbID = pdbID.upper()
    self[pdbID] = self.get(pdbID, {})
    self[pdbID][chainID] = sequence
    self.sequences.append((pdbID, chainID, sequence))
    if not self.unique_sequences.get(sequence):
        self.unique_sequences[sequence] = visible_colors[len(self.
            unique_sequences) % len(visible_colors)]
    self.identical_sequences = None