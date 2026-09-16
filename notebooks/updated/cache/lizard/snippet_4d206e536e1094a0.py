def openidf(fname, idd=None, epw=None):
    import eppy.easyopen as easyopen
    return easyopen.easyopen(fname, idd=idd, epw=epw)