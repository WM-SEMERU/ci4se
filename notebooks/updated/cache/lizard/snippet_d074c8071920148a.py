def decode_str(s, free=False):
    try:
        if s.len == 0:
            return ''
        return ffi.unpack(s.data, s.len).decode('utf-8', 'replace')
    finally:
        if free:
            lib.semaphore_str_free(ffi.addressof(s))