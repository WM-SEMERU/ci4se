def dna(self, loc, mask='lower', rev_comp=False, lowercase=False):
    l = libdna.parse_loc(loc)
    ret = self._read_dna(l, lowercase=lowercase)
    self._read_n(l, ret)
    self._read_mask(l, ret, mask=mask)
    if rev_comp:
        DNA2Bit._rev_comp(ret)
    ret = ret.decode('utf-8')
    if lowercase:
        ret = ret.lower()
    return ret