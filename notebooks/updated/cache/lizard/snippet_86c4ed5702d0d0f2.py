def from_extinction_model(cls, modelname, **kwargs):
    modelname = modelname.lower()
    if modelname == 'lmc30dor':
        cfgitem = Conf.lmc30dor_file
    elif modelname == 'lmcavg':
        cfgitem = Conf.lmcavg_file
    elif modelname == 'mwavg':
        cfgitem = Conf.mwavg_file
    elif modelname == 'mwdense':
        cfgitem = Conf.mwdense_file
    elif modelname == 'mwrv21':
        cfgitem = Conf.mwrv21_file
    elif modelname == 'mwrv40':
        cfgitem = Conf.mwrv40_file
    elif modelname == 'smcbar':
        cfgitem = Conf.smcbar_file
    elif modelname == 'xgalsb':
        cfgitem = Conf.xgal_file
    else:
        raise exceptions.SynphotError('Extinction model {0} is invalid.'.
            format(modelname))
    filename = cfgitem()
    if 'flux_unit' not in kwargs:
        kwargs['flux_unit'] = cls._internal_flux_unit
    if (filename.endswith('fits') or filename.endswith('fit')
        ) and 'flux_col' not in kwargs:
        kwargs['flux_col'] = 'Av/E(B-V)'
    header, wavelengths, rvs = specio.read_remote_spec(filename, **kwargs)
    header['filename'] = filename
    header['descrip'] = cfgitem.description
    meta = {'header': header, 'expr': modelname}
    return cls(Empirical1D, points=wavelengths, lookup_table=rvs, meta=meta)