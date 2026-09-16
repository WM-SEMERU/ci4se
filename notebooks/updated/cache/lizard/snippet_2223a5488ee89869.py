def estimate_size_in_bytes(cls, key, value, headers):
    return cls.HEADER_STRUCT.size + cls.MAX_RECORD_OVERHEAD + cls.size_of(key,
        value, headers)