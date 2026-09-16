def selectOptimalChunk(self, peer):
    have = sets.Set(self.mask.positions(1))
    want = sets.Set(self.peers[peer].mask.positions(0))
    exchangeable = have.intersection(want)
    finalSet = dict.fromkeys(exchangeable, 0)
    for chunkNumber in exchangeable:
        for otherPeer in self.peers.itervalues():
            finalSet[chunkNumber] += not otherPeer.mask[chunkNumber]
    rarityList = [(rarity, random.random(), chunkNumber) for chunkNumber,
        rarity in finalSet.iteritems()]
    if not rarityList:
        return None, None
    rarityList.sort()
    chunkNumber = rarityList[-1][-1]
    assert self.mask[chunkNumber], "I wanted to send a chunk I didn't have"
    self.file.seek(chunkNumber * CHUNK_SIZE)
    chunkData = self.file.read(CHUNK_SIZE)
    self.sha1sums[chunkNumber] = sha.new(chunkData).digest()
    return chunkNumber, chunkData