def subDict(self, tags, raw=False):
    retDict = {}
    for tag in tags:
        retDict[tag] = self.get(tag, raw=raw)
    return retDict