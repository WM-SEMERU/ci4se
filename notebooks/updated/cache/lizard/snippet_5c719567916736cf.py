def Size(self):
    corrected_items = list(map(lambda i: CoinState(i), self.Items))
    return super(UnspentCoinState, self).Size() + GetVarSize(corrected_items)