def str_between(str_, startstr, endstr):
    r
    if startstr is None:
        startpos = 0
    else:
        startpos = str_.find(startstr) + len(startstr)
    if endstr is None:
        endpos = None
    else:
        endpos = str_.find(endstr)
        if endpos == -1:
            endpos = None
    newstr = str_[startpos:endpos]
    return newstr