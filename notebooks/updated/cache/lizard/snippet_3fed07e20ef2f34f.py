def _gen_condition(cls, initial, new_public_keys):
    try:
        threshold = len(new_public_keys)
    except TypeError:
        threshold = None
    if isinstance(new_public_keys, list) and len(new_public_keys) > 1:
        ffill = ThresholdSha256(threshold=threshold)
        reduce(cls._gen_condition, new_public_keys, ffill)
    elif isinstance(new_public_keys, list) and len(new_public_keys) <= 1:
        raise ValueError('Sublist cannot contain single owner')
    else:
        try:
            new_public_keys = new_public_keys.pop()
        except AttributeError:
            pass
        if isinstance(new_public_keys, Fulfillment):
            ffill = new_public_keys
        else:
            ffill = Ed25519Sha256(public_key=base58.b58decode(new_public_keys))
    initial.add_subfulfillment(ffill)
    return initial