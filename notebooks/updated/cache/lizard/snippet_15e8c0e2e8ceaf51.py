def _in(self, *lst):
    self.terms.append('in (%s)' % ', '.join([('"%s"' % x) for x in lst]))
    return self