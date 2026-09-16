def writeDrizKeywords(hdr, imgnum, drizdict):
    _keyprefix = 'D%03d' % imgnum
    for key in drizdict:
        val = drizdict[key]['value']
        if val is None:
            val = ''
        comment = drizdict[key]['comment']
        if comment is None:
            comment = ''
        hdr[_keyprefix + key] = val, drizdict[key]['comment']