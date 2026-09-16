def doit(self):
    print('                . doit')
    lines = Lines()
    lines.add(1, 'cpdef inline void doit(self, int idx) %s:' % _nogil)
    lines.add(2, 'self.idx_sim = idx')
    if getattr(self.model.sequences, 'inputs', None) is not None:
        lines.add(2, 'self.load_data()')
    if self.model.INLET_METHODS:
        lines.add(2, 'self.update_inlets()')
    if hasattr(self.model, 'solve'):
        lines.add(2, 'self.solve()')
    else:
        lines.add(2, 'self.run()')
        if getattr(self.model.sequences, 'states', None) is not None:
            lines.add(2, 'self.new2old()')
    if self.model.OUTLET_METHODS:
        lines.add(2, 'self.update_outlets()')
    return lines