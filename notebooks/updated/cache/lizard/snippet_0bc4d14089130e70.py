def to_dict(self):
    res = self._asdict()
    res['kraus_ops'] = [[k.real.tolist(), k.imag.tolist()] for k in self.
        kraus_ops]
    return res