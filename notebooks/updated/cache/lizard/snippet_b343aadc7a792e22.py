def set_freqs(self, n, f_lo_ghz, f_hi_ghz):
    if not f_lo_ghz >= 0:
        raise ValueError('must have f_lo_ghz >= 0; got %r' % (f_lo_ghz,))
    if not f_hi_ghz >= f_lo_ghz:
        raise ValueError('must have f_hi_ghz >= f_lo_ghz; got %r, %r' % (
            f_hi_ghz, f_lo_ghz))
    if not n >= 1:
        raise ValueError('must have n >= 1; got %r' % (n,))
    self.in_vals[IN_VAL_NFREQ] = n
    self.in_vals[IN_VAL_FREQ0] = f_lo_ghz * 1000000000.0
    self.in_vals[IN_VAL_LOGDFREQ] = np.log10(f_hi_ghz / f_lo_ghz) / n
    return self