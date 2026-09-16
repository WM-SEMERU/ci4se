def copyPage(self, pno, to=-1):
    pl = list(range(len(self)))
    if pno < 0 or pno > pl[-1]:
        raise ValueError("'from' page number out of range")
    if to < -1 or to > pl[-1]:
        raise ValueError("'to' page number out of range")
    if to == -1:
        pl.append(pno)
    else:
        pl.insert(to, pno)
    return self.select(pl)