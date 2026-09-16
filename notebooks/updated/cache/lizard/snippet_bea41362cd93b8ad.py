def metadata(f):
    if not isinstance(f, segyio.SegyFile):
        with segyio.open(f) as fl:
            return metadata(fl)
    spec = segyio.spec()
    spec.iline = f._il
    spec.xline = f._xl
    spec.samples = f.samples
    spec.format = f.format
    spec.ilines = f.ilines
    spec.xlines = f.xlines
    spec.offsets = f.offsets
    spec.sorting = f.sorting
    spec.tracecount = f.tracecount
    spec.ext_headers = f.ext_headers
    spec.endian = f.endian
    return spec