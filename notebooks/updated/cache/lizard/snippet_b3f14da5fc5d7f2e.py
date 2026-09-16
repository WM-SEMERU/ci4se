def loadAnns(self, ids=[]):
    if _isArrayLike(ids):
        return [self.anns[id] for id in ids]
    elif type(ids) == int:
        return [self.anns[ids]]