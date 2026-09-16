def Header(self):
    if not self._header:
        self._header = Header(self.PrevHash, self.MerkleRoot, self.
            Timestamp, self.Index, self.ConsensusData, self.NextConsensus,
            self.Script)
    return self._header