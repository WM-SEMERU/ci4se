def _vectorize_single_raster(self, raster, data_transform, crs, timestamp=None
    ):
    mask = None
    if self.values:
        mask = np.zeros(raster.shape, dtype=np.bool)
        for value in self.values:
            mask[raster == value] = True
    geo_list = []
    value_list = []
    for idx in range(raster.shape[-1]):
        for geojson, value in rasterio.features.shapes(raster[..., idx],
            mask=None if mask is None else mask[..., idx], transform=
            data_transform):
            geo_list.append(shapely.geometry.shape(geojson))
            value_list.append(value)
    geo_series = GeoSeries(geo_list)
    value_series = GeoSeries(value_list)
    series_dict = dict(VALUE=value_series, geometry=geo_series
        ) if timestamp is None else dict(VALUE=value_series, TIMESTAMP=
        GeoSeries([timestamp] * len(geo_list)), geometry=geo_series)
    return GeoDataFrame(series_dict, crs={'init': 'epsg:{}'.format(crs.value)})