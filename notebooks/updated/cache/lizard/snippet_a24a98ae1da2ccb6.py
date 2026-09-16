def load_initial(self, streams):
    d = {}
    for stream in streams:
        s = io.load(stream)
        if 'BLOCK' not in s:
            raise ValueError('No BLOCK found')
        d.update(s['BLOCK'])
    d = {'BLOCK': d}
    C = io.wc_lha2dict(d)
    sm = io.sm_lha2dict(d)
    C.update(sm)
    C = definitions.symmetrize(C)
    self.C_in = C