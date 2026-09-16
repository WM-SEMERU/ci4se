def deletePageRange(self, from_page=-1, to_page=-1):
    pl = list(range(len(self)))
    f = from_page
    t = to_page
    if f == -1:
        f = pl[-1]
    if t == -1:
        t = pl[-1]
    if not 0 <= f <= t <= pl[-1]:
        raise ValueError('page number(s) out of range')
    for i in range(f, t + 1):
        pl.remove(i)
    return self.select(pl)