def parse_type(self, hdat, dataobj=None):
    try:
        dataobj = dataobj.dataobj
    except Exception:
        pass
    dtype = np.asarray(dataobj).dtype if dataobj else self.default_type()
    if hdat and 'type' in hdat:
        dtype = np.dtype(hdat['type'])
    elif hdat and 'dtype' in hdat:
        dtype = np.dtype(hdat['dtype'])
    return dtype