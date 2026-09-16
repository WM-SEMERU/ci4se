def buildNewRootname(filename, extn=None, extlist=None):
    _extlist = copy.deepcopy(EXTLIST)
    if extlist:
        _extlist += extlist
    if isinstance(filename, fits.HDUList):
        try:
            filename = filename.filename()
        except:
            raise ValueError(
                "Can't determine the filename of an waivered HDUList object.")
    for suffix in _extlist:
        _indx = filename.find(suffix)
        if _indx > 0:
            break
    if _indx < 0:
        _indx = len(filename)
    if extn is None:
        extn = ''
    return filename[:_indx] + extn