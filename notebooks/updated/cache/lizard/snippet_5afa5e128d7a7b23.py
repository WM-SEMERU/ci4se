def GetScriptHashesForVerifying(self):
    hashes = super(ClaimTransaction, self).GetScriptHashesForVerifying()
    for hash, group in groupby(self.Claims, lambda x: x.PrevHash):
        tx, height = Blockchain.Default().GetTransaction(hash)
        if tx is None:
            raise Exception('Invalid Claim Operation')
        for claim in group:
            if len(tx.outputs) <= claim.PrevIndex:
                raise Exception('Invalid Claim Operation')
            script_hash = tx.outputs[claim.PrevIndex].ScriptHash
            if script_hash not in hashes:
                hashes.append(script_hash)
    hashes.sort()
    return hashes