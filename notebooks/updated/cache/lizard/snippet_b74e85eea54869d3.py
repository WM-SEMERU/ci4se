def geis2mef(sciname, convert_dq=True):
    clobber = True
    mode = 'update'
    memmap = True
    try:
        fimg = readgeis.readgeis(sciname)
    except Exception:
        raise IOError('Could not open GEIS input: %s' % sciname)
    _dqname = fileutil.buildNewRootname(sciname, extn='.c1h')
    dqexists = os.path.exists(_dqname)
    if dqexists:
        try:
            dqfile = readgeis.readgeis(_dqname)
            dqfitsname = fileutil.buildFITSName(_dqname)
        except Exception:
            print('Could not read data quality file %s' % _dqname)
    fitsname = fileutil.buildFITSName(sciname)
    fexists = os.path.exists(fitsname)
    if fexists and clobber or not fexists:
        print('Writing out GEIS as MEF to ', fitsname)
        if ASTROPY_VER_GE13:
            fimg.writeto(fitsname, overwrite=clobber)
        else:
            fimg.writeto(fitsname, clobber=clobber)
        if dqexists:
            print('Writing out GEIS as MEF to ', dqfitsname)
            if ASTROPY_VER_GE13:
                dqfile.writeto(dqfitsname, overwrite=clobber)
            else:
                dqfile.writeto(dqfitsname, clobber=clobber)
    fimg.close()
    del fimg
    fimg = fits.open(fitsname, mode=mode, memmap=memmap)
    return fimg