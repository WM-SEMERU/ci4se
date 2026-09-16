def _primary_input(self, index):
    primary_input = z.ZcashByteData()
    primary_input += self.tx_joinsplits[index].anchor
    primary_input += self.tx_joinsplits[index].nullifiers
    primary_input += self.tx_joinsplits[index].commitments
    primary_input += self.tx_joinsplits[index].vpub_old
    primary_input += self.tx_joinsplits[index].vpub_new
    primary_input += self.hsigs[index]
    primary_input += self.tx_joinsplits[index].vmacs
    return primary_input.to_bytes()