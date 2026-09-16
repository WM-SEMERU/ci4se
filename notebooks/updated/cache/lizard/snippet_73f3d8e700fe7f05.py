def get_dataset(self, dataset_id, ds_info):
    msg = self._get_message(ds_info)
    ds_info = self.get_metadata(msg, ds_info)
    fill = msg['missingValue']
    data = msg.values.astype(np.float32)
    if msg.valid_key('jScansPositively') and msg['jScansPositively'] == 1:
        data = data[::-1]
    if isinstance(data, np.ma.MaskedArray):
        data = data.filled(np.nan)
        data = da.from_array(data, chunks=CHUNK_SIZE)
    else:
        data[data == fill] = np.nan
        data = da.from_array(data, chunks=CHUNK_SIZE)
    return xr.DataArray(data, attrs=ds_info, dims=('y', 'x'))