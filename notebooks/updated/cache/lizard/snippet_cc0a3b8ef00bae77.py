def quantity_to_hdf5(f, key, q):
    if hasattr(q, 'unit'):
        f[key] = q.value
        f[key].attrs['unit'] = str(q.unit)
    else:
        f[key] = q
        f[key].attrs['unit'] = ''