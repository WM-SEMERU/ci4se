def c32ToB58(c32string, version=-1):
    addr_version, addr_hash160 = c32addressDecode(c32string)
    bitcoin_version = None
    if version < 0:
        bitcoin_version = addr_version
        if ADDR_STACKS_TO_BITCOIN.get(addr_version) is not None:
            bitcoin_version = ADDR_STACKS_TO_BITCOIN[addr_version]
    else:
        bitcoin_version = version
    return keylib.b58check.b58check_encode(addr_hash160.decode('hex'),
        bitcoin_version)