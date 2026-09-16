def GetBlockByHeight(self, height):
    hash = self.GetBlockHash(height)
    if hash is not None:
        return self.GetBlockByHash(hash)