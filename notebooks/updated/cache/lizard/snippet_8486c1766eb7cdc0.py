def encrypt(self, data):
    if False in six.itervalues(self.ready):
        raise CipherError(data)
    encryptor = self._cipher.encryptor()
    tmp = encryptor.update(data) + encryptor.finalize()
    self.iv = tmp[-self.block_size:]
    return tmp