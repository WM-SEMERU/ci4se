def open(filename, mode='r', iline=189, xline=193, strict=True,
    ignore_geometry=False, endian='big'):
    if 'w' in mode:
        problem = 'w in mode would truncate the file'
        solution = 'use r+ to open in read-write'
        raise ValueError(', '.join((problem, solution)))
    endians = {'little': 256, 'lsb': 256, 'big': 0, 'msb': 0}
    if endian not in endians:
        problem = 'unknown endianness {}, expected one of: '
        opts = ' '.join(endians.keys())
        raise ValueError(problem.format(endian) + opts)
    from . import _segyio
    fd = _segyio.segyiofd(str(filename), mode, endians[endian])
    fd.segyopen()
    metrics = fd.metrics()
    f = segyio.SegyFile(fd, filename=str(filename), mode=mode, iline=iline,
        xline=xline, endian=endian)
    try:
        dt = segyio.tools.dt(f, fallback_dt=4000.0) / 1000.0
        t0 = f.header[0][segyio.TraceField.DelayRecordingTime]
        samples = metrics['samplecount']
        f._samples = numpy.arange(samples) * dt + t0
    except:
        f.close()
        raise
    if ignore_geometry:
        return f
    return infer_geometry(f, metrics, iline, xline, strict)