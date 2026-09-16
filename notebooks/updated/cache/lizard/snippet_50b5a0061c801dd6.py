def set_prior(self, prior, warning=True):
    repriorized = self.unset_priors()
    self._add_to_index_operations(self.priors, repriorized, prior, warning)
    from paramz.domains import _REAL, _POSITIVE, _NEGATIVE
    if prior.domain is _POSITIVE:
        self.constrain_positive(warning)
    elif prior.domain is _NEGATIVE:
        self.constrain_negative(warning)
    elif prior.domain is _REAL:
        rav_i = self._raveled_index()
        assert all(all(False if c is __fixed__ else c.domain is _REAL for c in
            con) for con in self.constraints.properties_for(rav_i)
            ), 'Domain of prior and constraint have to match, please unconstrain if you REALLY wish to use this prior'