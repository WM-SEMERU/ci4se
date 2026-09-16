def parse_redis_url(url):
    warnings.warn('Use redis.StrictRedis.from_url instead',
        DeprecationWarning, stacklevel=2)
    parsed = urllib.parse.urlsplit(url)
    return {'host': parsed.hostname, 'port': parsed.port, 'db': int(parsed.
        path.replace('/', ''))}