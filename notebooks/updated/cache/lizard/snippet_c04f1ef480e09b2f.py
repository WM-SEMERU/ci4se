def GetCoinAssets(self):
    assets = set()
    for coin in self.GetCoins():
        assets.add(coin.Output.AssetId)
    return list(assets)