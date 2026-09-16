def crypto_pwhash_str_verify(passwd_hash, passwd):
    ensure(isinstance(passwd_hash, bytes), raising=TypeError)
    ensure(isinstance(passwd, bytes), raising=TypeError)
    ensure(len(passwd_hash) <= 127, 'Hash must be at most 127 bytes long',
        raising=exc.ValueError)
    ret = lib.crypto_pwhash_str_verify(passwd_hash, passwd, len(passwd))
    ensure(ret == 0, 'Wrong password', raising=exc.InvalidkeyError)
    return True