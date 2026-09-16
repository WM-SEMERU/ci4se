def cumsum(self, axis=0, *args, **kwargs):
    nv.validate_cumsum(args, kwargs)
    if axis is None:
        axis = self._stat_axis_number
    return self.apply(lambda x: x.cumsum(), axis=axis)