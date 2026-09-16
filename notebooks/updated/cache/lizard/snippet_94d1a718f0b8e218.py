def _init_associations(self, fin_gpad, hdr_only=False):
    ini = InitAssc(fin_gpad, self.godag)
    nts = ini.init_associations(hdr_only)
    self.hdr = ini.hdr
    return nts