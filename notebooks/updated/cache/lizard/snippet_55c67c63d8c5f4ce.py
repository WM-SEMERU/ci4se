def get_key(cls, k, default=None):
    k = cls.__name__ + '__' + k
    if k in session:
        return session[k]
    else:
        return default