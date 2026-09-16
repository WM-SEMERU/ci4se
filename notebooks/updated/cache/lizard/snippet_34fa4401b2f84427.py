def generic_decrypt(cipher_factory_map, ciphertext, key, iv):
    if backend is None:
        raise PysnmpCryptoError('Crypto backend not available')
    return _DECRYPT_MAP[backend](cipher_factory_map[backend], ciphertext,
        key, iv)