def _setrow(self, row):
    try:
        compname, kwd, innode, outnode, thcomp = row[0:5]
    except ValueError:
        raise ValueError('Error unpacking row: %s' % row)
    k = int(innode)
    if compname == 'clear':
        compname = None
    if thcomp == 'clear':
        thcomp = None
    if kwd == 'default':
        self.tab[k].set_default(int(outnode), compname, thcomp)
    else:
        try:
            self.tab[k].set_named(kwd, int(outnode), compname, thcomp)
        except IndexError:
            old = self.tab[k].get_named(kwd)
            plist = k, kwd, old, (outnode, compname, thcomp)
            self.problemset.add(plist)