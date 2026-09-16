def convert2wavenumber(rsr):
    retv = {}
    for chname in rsr.keys():
        retv[chname] = {}
        for det in rsr[chname].keys():
            retv[chname][det] = {}
            if 'wavenumber' in rsr[chname][det].keys():
                retv[chname][det] = rsr[chname][det].copy()
                LOG.debug(
                    'RSR data already in wavenumber space. No conversion needed.'
                    )
                continue
            for sat in rsr[chname][det].keys():
                if sat == 'wavelength':
                    wnum = 1.0 / (0.0001 * rsr[chname][det][sat])
                    retv[chname][det]['wavenumber'] = wnum[::-1]
                elif sat == 'response':
                    if type(rsr[chname][det][sat]) is dict:
                        retv[chname][det][sat] = {}
                        for name in rsr[chname][det][sat].keys():
                            resp = rsr[chname][det][sat][name]
                            retv[chname][det][sat][name] = resp[::-1]
                    else:
                        resp = rsr[chname][det][sat]
                        retv[chname][det][sat] = resp[::-1]
    unit = 'cm-1'
    si_scale = 100.0
    return retv, {'unit': unit, 'si_scale': si_scale}