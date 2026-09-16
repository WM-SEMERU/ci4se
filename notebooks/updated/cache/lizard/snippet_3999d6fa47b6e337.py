def reindex(self, kdims=[], force=False):
    if not isinstance(kdims, list):
        kdims = [kdims]
    kdims = [self.get_dimension(kd, strict=True) for kd in kdims]
    dropped = [kd for kd in self.kdims if kd not in kdims]
    if dropped:
        raise ValueError(
            'DynamicMap does not allow dropping dimensions, reindex may only be used to reorder dimensions.'
            )
    return super(DynamicMap, self).reindex(kdims, force)