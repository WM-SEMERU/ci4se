def lineincustcols(inlist, colsizes):
    outstr = ''
    for i in range(len(inlist)):
        if type(inlist[i]) != StringType:
            item = str(inlist[i])
        else:
            item = inlist[i]
        size = len(item)
        if size <= colsizes[i]:
            for j in range(colsizes[i] - size):
                outstr = outstr + ' '
            outstr = outstr + item
        else:
            outstr = outstr + item[0:colsizes[i] + 1]
    return outstr