def sample(self, fields=None, count=5, sampling=None, use_cache=True,
    dialect=None, billing_tier=None):
    return self._table.sample(fields=fields, count=count, sampling=sampling,
        use_cache=use_cache, dialect=dialect, billing_tier=billing_tier)