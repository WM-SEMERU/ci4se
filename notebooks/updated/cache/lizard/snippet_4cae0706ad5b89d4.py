def _prepare_key(key, *args, **kwargs):
    if not args and not kwargs:
        return key
    items = sorted(kwargs.items())
    hashable_args = args, tuple(items)
    args_key = hashlib.md5(pickle.dumps(hashable_args)).hexdigest()
    return '%s/args:%s' % (key, args_key)