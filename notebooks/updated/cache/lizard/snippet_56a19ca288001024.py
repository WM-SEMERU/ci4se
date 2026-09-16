def encode(obj, sedes=None, infer_serializer=True, cache=True):
    if isinstance(obj, Serializable):
        cached_rlp = obj._cached_rlp
        if sedes is None and cached_rlp:
            return cached_rlp
        else:
            really_cache = cache and sedes is None
    else:
        really_cache = False
    if sedes:
        item = sedes.serialize(obj)
    elif infer_serializer:
        item = infer_sedes(obj).serialize(obj)
    else:
        item = obj
    result = encode_raw(item)
    if really_cache:
        obj._cached_rlp = result
    return result