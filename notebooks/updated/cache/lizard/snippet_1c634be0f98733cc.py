def crypto_pwhash_scryptsalsa208sha256_ll(passwd, salt, n, r, p, dklen=64,
    maxmem=SCRYPT_MAX_MEM):
    ensure(isinstance(n, integer_types), raising=TypeError)
    ensure(isinstance(r, integer_types), raising=TypeError)
    ensure(isinstance(p, integer_types), raising=TypeError)
    ensure(isinstance(passwd, bytes), raising=TypeError)
    ensure(isinstance(salt, bytes), raising=TypeError)
    _check_memory_occupation(n, r, p, maxmem)
    buf = ffi.new('uint8_t[]', dklen)
    ret = lib.crypto_pwhash_scryptsalsa208sha256_ll(passwd, len(passwd),
        salt, len(salt), n, r, p, buf, dklen)
    ensure(ret == 0, 'Unexpected failure in key derivation', raising=exc.
        RuntimeError)
    return ffi.buffer(ffi.cast('char *', buf), dklen)[:]