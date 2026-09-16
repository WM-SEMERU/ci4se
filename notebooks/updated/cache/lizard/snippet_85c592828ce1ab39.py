def mad(var, constant=1):
    median = np.median(var)
    mad = np.median(np.abs(var - median))
    mad = mad * constant
    return mad