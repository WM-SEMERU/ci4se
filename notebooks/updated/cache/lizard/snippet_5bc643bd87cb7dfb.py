def calc_checksum(self, expanded=False):
    if expanded:
        cs = [int(np.sum(self.e_d_signal[ch]) % 65536) for ch in range(self
            .n_sig)]
    else:
        cs = np.sum(self.d_signal, 0) % 65536
        cs = [int(c) for c in cs]
    return cs