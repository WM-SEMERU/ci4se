def buid(valu=None):
    if valu is None:
        return os.urandom(32)
    byts = s_msgpack.en(valu)
    return hashlib.sha256(byts).digest()