def accept_totp(key, response, format='dec6', period=30, t=None, hash=
    hashlib.sha1, forward_drift=1, backward_drift=1, drift=0):
    if t is None:
        t = int(time.time())
    for i in range(max(-divmod(t, period)[0], -backward_drift), 
        forward_drift + 1):
        d = (drift + i) * period
        if _utils.compare_digest(totp(key, format=format, period=period,
            hash=hash, t=t + d), response):
            return True, drift + i
    return False, 0