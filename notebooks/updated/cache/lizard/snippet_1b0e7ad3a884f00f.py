def create_random(magf, magf_params, errf, errf_params, timef=np.linspace,
    timef_params=None, size=DEFAULT_SIZE, id=None, ds_name=DS_NAME,
    description=DESCRIPTION, bands=BANDS, metadata=METADATA):
    timef_params = {'start': 0.0, 'stop': 1.0
        } if timef_params is None else timef_params.copy()
    timef_params.update(num=size)
    magf_params = magf_params.copy()
    magf_params.update(size=size)
    errf_params = errf_params.copy()
    errf_params.update(size=size)
    data = {}
    for band in bands:
        data[band] = {'time': timef(**timef_params), 'magnitude': magf(**
            magf_params), 'error': errf(**errf_params)}
    return Data(id=id, ds_name=ds_name, description=description, bands=
        bands, metadata=metadata, data=data)