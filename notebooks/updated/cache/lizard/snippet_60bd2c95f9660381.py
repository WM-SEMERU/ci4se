def from_file(filename, use_cores=True, thresh=0.0001):
    with zopen(filename, 'rt') as f:
        return Xr.from_string(f.read(), use_cores=use_cores, thresh=thresh)