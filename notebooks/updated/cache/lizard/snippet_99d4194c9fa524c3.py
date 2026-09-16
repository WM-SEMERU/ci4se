def set_bfield(self, B_G):
    if not B_G > 0:
        raise ValueError('must have B_G > 0; got %r' % (B_G,))
    self.in_vals[IN_VAL_B] = B_G
    return self