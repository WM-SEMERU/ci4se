def cfitsio_version(asfloat=False):
    ver = '%0.3f' % _fitsio_wrap.cfitsio_version()
    if asfloat:
        return float(ver)
    else:
        return ver