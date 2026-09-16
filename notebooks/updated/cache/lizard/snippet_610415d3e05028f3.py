def from_b58check(private_key):
    b58dec = base58.b58decode_check(private_key)
    version = b58dec[0]
    assert version in [PrivateKey.TESTNET_VERSION, PrivateKey.MAINNET_VERSION]
    return PrivateKey(int.from_bytes(b58dec[1:], 'big'))