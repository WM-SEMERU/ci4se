def sign(mv):
    md5 = hashlib.md5()
    update_hash(md5, mv)
    return md5.digest()