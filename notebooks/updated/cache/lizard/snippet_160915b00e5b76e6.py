def blake2b(data, digest_size=BLAKE2B_BYTES, key=b'', salt=b'', person=b'',
    encoder=nacl.encoding.HexEncoder):
    digest = _b2b_hash(data, digest_size=digest_size, key=key, salt=salt,
        person=person)
    return encoder.encode(digest)