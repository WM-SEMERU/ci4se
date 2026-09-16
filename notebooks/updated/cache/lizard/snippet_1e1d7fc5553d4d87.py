def add_rdataset(self, section, name, rdataset, **kw):
    self._set_section(section)
    before = self.output.tell()
    n = rdataset.to_wire(name, self.output, self.compress, self.origin, **kw)
    after = self.output.tell()
    if after >= self.max_size:
        self._rollback(before)
        raise dns.exception.TooBig
    self.counts[section] += n