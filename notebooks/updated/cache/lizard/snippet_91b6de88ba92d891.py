def execute(self, eopatch):
    data_arr = eopatch[FeatureType.MASK]['IS_DATA']
    _, height, width, _ = data_arr.shape
    request = self._get_wms_request(eopatch.bbox, width, height)
    request_data, = np.asarray(request.get_data())
    if isinstance(self.raster_value, dict):
        raster = self._map_from_multiclass(eopatch, (height, width),
            request_data)
    elif isinstance(self.raster_value, (int, float)):
        raster = self._map_from_binaries(eopatch, (height, width), request_data
            )
    else:
        raise ValueError('Unsupported raster value type')
    if self.feature_type is FeatureType.MASK_TIMELESS and raster.ndim == 2:
        raster = raster[..., np.newaxis]
    eopatch[self.feature_type][self.feature_name] = raster
    return eopatch