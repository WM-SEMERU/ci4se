def hashleftjoin(left, right, key=None, lkey=None, rkey=None, missing=None,
    cache=True, lprefix=None, rprefix=None):
    lkey, rkey = keys_from_args(left, right, key, lkey, rkey)
    return HashLeftJoinView(left, right, lkey, rkey, missing=missing, cache
        =cache, lprefix=lprefix, rprefix=rprefix)