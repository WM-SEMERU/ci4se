def _group(self, taxslice):
    res = []
    while taxslice:
        taxref, lident = taxslice.pop()
        if lident == '':
            res.append(([taxref], lident))
        else:
            i = 0
            group = []
            while i < len(taxslice):
                if taxslice[i][1] == lident:
                    group.append(taxslice.pop(i)[0])
                else:
                    i += 1
            group.append(taxref)
            res.append((group, lident))
    return res