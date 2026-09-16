def write(self, df, table_name, temp_dir=CACHE_DIR, overwrite=False, lnglat
    =None, encode_geom=False, geom_col=None, **kwargs):
    tqdm.write(
        'Params: encode_geom, geom_col and everything in kwargs are deprecated and not being used any more'
        )
    dataset = Dataset(self, table_name, df=df)
    if_exists = Dataset.FAIL
    if overwrite:
        if_exists = Dataset.REPLACE
    dataset = dataset.upload(with_lonlat=lnglat, if_exists=if_exists)
    tqdm.write('Table successfully written to CARTO: {table_url}'.format(
        table_url=utils.join_url(self.creds.base_url(), 'dataset', dataset.
        table_name)))
    return dataset