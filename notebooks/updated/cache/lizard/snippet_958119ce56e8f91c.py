def ed25519_generate_key_pair_from_secret(secret):
    if not isinstance(secret, bytes):
        secret = secret.encode()
    hash_bytes = sha3.keccak_256(secret).digest()
    sk = Ed25519SigningKeyFromHash.generate(hash_bytes=hash_bytes)
    private_value_base58 = sk.encode(encoding='base58')
    public_value_compressed_base58 = sk.get_verifying_key().encode(encoding
        ='base58')
    return private_value_base58, public_value_compressed_base58