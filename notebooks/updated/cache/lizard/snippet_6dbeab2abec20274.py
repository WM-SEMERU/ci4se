def load_data(filespec, idx=None, logger=None, **kwargs):
    global loader_registry
    info = iohelper.get_fileinfo(filespec)
    filepath = info.filepath
    if idx is None:
        idx = info.numhdu
    try:
        typ, subtyp = iohelper.guess_filetype(filepath)
    except Exception as e:
        if logger is not None:
            logger.warning(
                "error determining file type: %s; assuming 'image/fits'" %
                str(e))
        typ, subtyp = 'image', 'fits'
    if logger is not None:
        logger.debug("assuming file type: %s/%s'" % (typ, subtyp))
    try:
        loader_info = loader_registry['%s/%s' % (typ, subtyp)]
        data_loader = loader_info.loader
    except KeyError:
        data_loader = load_fits
    data_obj = data_loader(filepath, idx=idx, logger=logger, **kwargs)
    return data_obj