def kdf(size, password, salt, opslimit=OPSLIMIT_SENSITIVE, memlimit=
    MEMLIMIT_SENSITIVE, encoder=nacl.encoding.RawEncoder):
    ensure(len(salt) == SALTBYTES, 
        'The salt must be exactly %s, not %s bytes long' % (SALTBYTES, len(
        salt)), raising=exc.ValueError)
    n_log2, r, p = nacl.bindings.nacl_bindings_pick_scrypt_params(opslimit,
        memlimit)
    maxmem = memlimit + 2 ** 16
    return encoder.encode(nacl.bindings.
        crypto_pwhash_scryptsalsa208sha256_ll(password, salt, 2 ** n_log2,
        r, p, maxmem=maxmem, dklen=size))