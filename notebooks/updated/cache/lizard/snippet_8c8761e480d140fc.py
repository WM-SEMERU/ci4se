def aggregate_periods(self, periods):
    try:
        fieldname = self.raster_field.name
    except TypeError:
        raise exceptions.FieldDoesNotExist('Raster field not found')
    arrays = self.arrays(fieldname)
    arr = arrays[0]
    if len(arrays) > 1:
        if getattr(arr, 'ndim', 0) > 2:
            arrays = np.vstack(arrays)
        fill = getattr(arr, 'fill_value', None)
        arr = np.ma.masked_values(arrays, fill, copy=False)
    try:
        means = arr.reshape((periods, -1)).mean(axis=1)
    except ValueError:
        means = np.array([a.mean() for a in np.array_split(arr, periods)])
    obj = self[0]
    setattr(obj, fieldname, means)
    return [obj]