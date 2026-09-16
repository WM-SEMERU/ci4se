def value_name(cls, value):
    for k, v in list(cls.__dict__.items()):
        if v == value:
            return k
    return value