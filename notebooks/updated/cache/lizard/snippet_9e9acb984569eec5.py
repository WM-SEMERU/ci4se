def convert_ints_floats(self, flds):
    for idx in self.idxs_float:
        flds[idx] = float(flds[idx])
    for idx in self.idxs_int:
        dig = flds[idx]
        flds[idx] = int(flds[idx]) if dig.isdigit() else dig
    for idx in self.idxs_strpat:
        hdr = self.hdr2idx.items()[idx][0]
        pat = self.strpat_hdrs[hdr]
        flds[idx] = pat.format(flds[idx])