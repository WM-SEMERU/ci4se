def _module_dir(handle):
    cache_dir = resolver.tfhub_cache_dir(use_temp=True)
    return resolver.create_local_module_dir(cache_dir, hashlib.sha1(handle.
        encode('utf8')).hexdigest())