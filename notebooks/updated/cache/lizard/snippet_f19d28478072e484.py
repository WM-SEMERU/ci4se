def dim_extents(self, *args, **kwargs):
    l = self.dim_lower_extent(*args, **kwargs)
    u = self.dim_upper_extent(*args, **kwargs)
    if isinstance(l, collections.Sequence):
        return zip(l, u)
    else:
        return l, u