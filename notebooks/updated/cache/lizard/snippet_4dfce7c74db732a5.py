def decode_pubkey_hex(pubkey_hex):
    if not isinstance(pubkey_hex, (str, unicode)):
        raise ValueError('public key is not a string')
    pubk = keylib.key_formatting.decompress(str(pubkey_hex))
    assert len(pubk) == 130
    pubk_raw = pubk[2:]
    pubk_i = int(pubk_raw[:64], 16), int(pubk_raw[64:], 16)
    return pubk_i