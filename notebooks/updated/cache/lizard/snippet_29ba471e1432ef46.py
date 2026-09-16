def FindUnspentCoinsByAsset(self, asset_id, from_addr=None, use_standard=
    False, watch_only_val=0):
    coins = self.FindUnspentCoins(from_addr=from_addr, use_standard=
        use_standard, watch_only_val=watch_only_val)
    return [coin for coin in coins if coin.Output.AssetId == asset_id]