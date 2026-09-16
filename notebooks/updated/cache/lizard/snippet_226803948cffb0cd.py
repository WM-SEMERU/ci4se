def set_key(cls, k, v):
    k = cls.__name__ + '__' + k
    session[k] = v