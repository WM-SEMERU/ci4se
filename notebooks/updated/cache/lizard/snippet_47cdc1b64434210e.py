def decompress_pubkey(pubkey, curve_name):
    vk = None
    if len(pubkey) == 33:
        decompress = {CURVE_NIST256: _decompress_nist256, CURVE_ED25519:
            _decompress_ed25519, ECDH_CURVE25519: _decompress_ed25519}[
            curve_name]
        vk = decompress(pubkey)
    if not vk:
        msg = 'invalid {!s} public key: {!r}'.format(curve_name, pubkey)
        raise ValueError(msg)
    return vk