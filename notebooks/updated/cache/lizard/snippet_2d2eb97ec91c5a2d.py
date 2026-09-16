def _uniq(self):
    pd = []
    for d in range(1, self.maxdepth):
        pd.extend(map(lambda x: int(4 ** (d + 1) + x), self.pixeldict[d]))
    return sorted(pd)