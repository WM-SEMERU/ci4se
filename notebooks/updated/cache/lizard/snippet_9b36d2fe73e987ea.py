def new(cls, alias, cert):
    timestamp = int(time.time()) * 1000
    tke = cls(timestamp=timestamp, alias=alias.lower(), cert=cert)
    return tke