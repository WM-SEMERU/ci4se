def encrypt(self, plaintext, nonce=None, encoder=encoding.RawEncoder):
    if nonce is None:
        nonce = random(self.NONCE_SIZE)
    if len(nonce) != self.NONCE_SIZE:
        raise exc.ValueError('The nonce must be exactly %s bytes long' %
            self.NONCE_SIZE)
    ciphertext = nacl.bindings.crypto_secretbox(plaintext, nonce, self._key)
    encoded_nonce = encoder.encode(nonce)
    encoded_ciphertext = encoder.encode(ciphertext)
    return EncryptedMessage._from_parts(encoded_nonce, encoded_ciphertext,
        encoder.encode(nonce + ciphertext))