def values(obj, glob, separator='/', afilter=None, dirs=True):
    return [x[1] for x in dpath.util.search(obj, glob, yielded=True,
        separator=separator, afilter=afilter, dirs=dirs)]