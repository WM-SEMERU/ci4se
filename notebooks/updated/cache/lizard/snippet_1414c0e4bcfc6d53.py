def beta_r(self, r, kwargs):
    if self._type == 'const':
        return self.const_beta(kwargs)
    elif self._type == 'OsipkovMerritt':
        return self.ospikov_meritt(r, kwargs)
    elif self._type == 'Colin':
        return self.colin(r, kwargs)
    elif self._type == 'isotropic':
        return self.isotropic()
    elif self._type == 'radial':
        return self.radial()
    else:
        raise ValueError('anisotropy type %s not supported!' % self._type)