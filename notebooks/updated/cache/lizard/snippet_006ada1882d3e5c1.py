def create_unique_wcsname(fimg, extnum, wcsname):
    wnames = list(wcsutil.altwcs.wcsnames(fimg, ext=extnum).values())
    if wcsname not in wnames:
        uniqname = wcsname
    else:
        rpatt = re.compile(wcsname + '_\\d')
        index = 0
        for wname in wnames:
            rmatch = rpatt.match(wname)
            if rmatch:
                n = int(wname[wname.rfind('_') + 1:])
                if n > index:
                    index = 1
        index += 1
        uniqname = '%s_%d' % (wcsname, index)
    return uniqname