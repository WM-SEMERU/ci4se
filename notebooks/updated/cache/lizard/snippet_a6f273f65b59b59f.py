def antijoin(left, right, key=None, lkey=None, rkey=None, presorted=False,
    buffersize=None, tempdir=None, cache=True):
    lkey, rkey = keys_from_args(left, right, key, lkey, rkey)
    return AntiJoinView(left=left, right=right, lkey=lkey, rkey=rkey,
        presorted=presorted, buffersize=buffersize, tempdir=tempdir, cache=
        cache)