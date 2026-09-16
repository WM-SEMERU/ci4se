def disp(name=None, idx=None):
    return CMADataLogger(name if name else CMADataLogger.default_prefix).disp(
        idx)