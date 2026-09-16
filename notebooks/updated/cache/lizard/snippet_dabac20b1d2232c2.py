def FindUnspentCoinsByAssetAndTotal(self, asset_id, amount, from_addr=None,
    use_standard=False, watch_only_val=0, reverse=False):
    coins = self.FindUnspentCoinsByAsset(asset_id, from_addr=from_addr,
        use_standard=use_standard, watch_only_val=watch_only_val)
    sum = Fixed8(0)
    for coin in coins:
        sum = sum + coin.Output.Value
    if sum < amount:
        return None
    coins = sorted(coins, key=lambda coin: coin.Output.Value.value)
    if reverse:
        coins.reverse()
    total = Fixed8(0)
    for coin in coins:
        if coin.Output.Value == amount:
            return [coin]
    to_ret = []
    for coin in coins:
        total = total + coin.Output.Value
        to_ret.append(coin)
        if total >= amount:
            break
    return to_ret