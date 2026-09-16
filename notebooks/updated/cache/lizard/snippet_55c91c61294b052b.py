def get_etag(storage, path, prefixed_path):
    cache_key = get_cache_key(path)
    etag = cache.get(cache_key, False)
    if etag is False:
        etag = get_remote_etag(storage, prefixed_path)
        cache.set(cache_key, etag)
    return etag