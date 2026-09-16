def from_dict(d):
    if d is None:
        return None
    return Response(d.get('html'), CacheInfo.from_dict(d.get('cache_info')),
        d.get('scraped'), d.get('raw'))