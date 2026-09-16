def _cryptography_decrypt(cipher_factory, ciphertext, key, iv):
    decryptor = cipher_factory(key, iv).decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()