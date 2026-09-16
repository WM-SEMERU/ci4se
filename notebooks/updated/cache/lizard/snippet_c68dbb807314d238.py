def _has_base(cls, base):
    if cls is base:
        return True
    elif cls is None:
        return False
    try:
        for bs in cls.__bases__:
            if _has_base(bs, base):
                return True
    except:
        pass
    return False