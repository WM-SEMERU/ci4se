def channel_names(self, usecols=None):
    if self.decdel == '.':
        datcnt = self.matches_p[self.rts]
    elif self.decdel == ',':
        datcnt = self.matches_c[self.rts]
    if usecols and max(usecols) >= datcnt:
        mess = ' Max column index is '
        raise IndexError(str(usecols) + mess + str(datcnt - 1))
    names = None
    if not self.rts:
        return None
    for row in self.rows[self.rts - 1::-1]:
        splitlist = row.split(self.datdel)
        for i, word in enumerate(splitlist):
            if not word.strip().startswith(ALPHAS):
                break
            elif i + 1 == datcnt:
                names = [ch.strip() for ch in splitlist[:datcnt]]
                break
        if names:
            break
    if usecols:
        names = [names[i] for i in sorted(usecols)]
    return names