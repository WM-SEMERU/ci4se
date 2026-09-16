def _compute_fingerprint(key):
    n = TLObject.serialize_bytes(get_byte_array(key.n))
    e = TLObject.serialize_bytes(get_byte_array(key.e))
    return struct.unpack('<q', sha1(n + e).digest()[-8:])[0]