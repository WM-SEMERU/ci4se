def _renew_by(name, window=None):
    expiry = _expires(name)
    if window is not None:
        expiry = expiry - datetime.timedelta(days=window)
    return expiry