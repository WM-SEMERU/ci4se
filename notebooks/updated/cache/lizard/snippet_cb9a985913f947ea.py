def auth_encrypt(self, P, A, seq_num):
    if False in six.itervalues(self.ready):
        raise CipherError(P, A)
    if hasattr(self, 'pc_cls'):
        self._cipher.mode._tag = None
        self._cipher.mode._initialization_vector = self._get_nonce(seq_num)
        encryptor = self._cipher.encryptor()
        encryptor.authenticate_additional_data(A)
        res = encryptor.update(P) + encryptor.finalize()
        res += encryptor.tag
    elif conf.crypto_valid_advanced and isinstance(self._cipher, AESCCM):
        res = self._cipher.encrypt(self._get_nonce(seq_num), P, A,
            tag_length=self.tag_len)
    else:
        res = self._cipher.encrypt(self._get_nonce(seq_num), P, A)
    return res