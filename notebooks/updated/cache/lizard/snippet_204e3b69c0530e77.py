def asodict(self, handlepoints=True, reportpoints=True):
    out = odict()
    if handlepoints:
        for hp in self.handlepoints:
            out[hp.hpoint] = hp.trace
    if reportpoints:
        for rp in self.reportpoints:
            if not rp.rpoint in out:
                out[rp.rpoint] = odict()
            out[rp.rpoint][self.attribute] = {'value': rp.value, 'extended':
                rp.extended}
    return out