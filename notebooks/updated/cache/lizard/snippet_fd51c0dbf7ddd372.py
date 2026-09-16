def FindUnspentCoins(self, from_addr=None, use_standard=False, watch_only_val=0
    ):
    ret = []
    for coin in self.GetCoins():
        if (coin.State & CoinState.Confirmed > 0 and coin.State & CoinState
            .Spent == 0 and coin.State & CoinState.Locked == 0 and coin.
            State & CoinState.Frozen == 0 and coin.State & CoinState.
            WatchOnly == watch_only_val):
            do_exclude = False
            if self._vin_exclude:
                for to_exclude in self._vin_exclude:
                    if (coin.Reference.PrevIndex == to_exclude.PrevIndex and
                        coin.Reference.PrevHash == to_exclude.PrevHash):
                        do_exclude = True
            if do_exclude:
                continue
            if from_addr is not None:
                if coin.Output.ScriptHash == from_addr:
                    ret.append(coin)
            elif use_standard:
                contract = self._contracts[coin.Output.ScriptHash.ToBytes()]
                if contract.IsStandard:
                    ret.append(coin)
            else:
                ret.append(coin)
    return ret