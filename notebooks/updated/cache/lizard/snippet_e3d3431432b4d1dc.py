def to_xarray_dataset(self, datasets=None):
    if datasets is not None:
        datasets = [self[ds] for ds in datasets]
    else:
        datasets = [self.datasets.get(ds) for ds in self.wishlist]
        datasets = [ds for ds in datasets if ds is not None]
    ds_dict = {i.attrs['name']: i.rename(i.attrs['name']) for i in datasets if
        i.attrs.get('area') is not None}
    mdata = combine_metadata(*tuple(i.attrs for i in datasets))
    if mdata.get('area') is None or not isinstance(mdata['area'],
        SwathDefinition):
        ds = xr.merge(ds_dict.values())
    else:
        lons, lats = mdata['area'].get_lonlats()
        if not isinstance(lons, DataArray):
            lons = DataArray(lons, dims=('y', 'x'))
            lats = DataArray(lats, dims=('y', 'x'))
        ds = xr.Dataset(ds_dict, coords={'latitude': (['y', 'x'], lats),
            'longitude': (['y', 'x'], lons)})
    ds.attrs = mdata
    return ds