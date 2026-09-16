def APO(series, fast=12, slow=26, matype=0):
    return _series_to_series(series, talib.APO, fast, slow, matype)