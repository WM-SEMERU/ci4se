def get_cache_key(bucket, name, args, kwargs):
    u = ''.join(map(str, (bucket, name, args, kwargs)))
    return 'native_tags.%s' % sha_constructor(u).hexdigest()