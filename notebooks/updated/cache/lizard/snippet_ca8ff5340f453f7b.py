def get_dataset(self, dsid, dsinfo):
    data = self[dsinfo.get('file_key', dsid.name)]
    data.attrs.update(dsinfo)
    data.attrs['platform_name'] = self['/attr/satellite_name']
    data.attrs['sensor'] = self['/attr/instrument_name']
    return data