def is_metatype(rdtype):
    if rdtype >= TKEY and rdtype <= ANY or rdtype in _metatypes:
        return True
    return False