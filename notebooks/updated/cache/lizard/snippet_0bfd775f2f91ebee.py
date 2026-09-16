def take(self, indices, axis=0, out=None, mode='raise'):
    return take_haplotype_array(self, indices, axis=axis, cls=type(self),
        take=np.take, out=out, mode=mode)