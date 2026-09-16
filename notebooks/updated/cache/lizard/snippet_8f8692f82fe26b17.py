def _GetServerCipher(self):
    if self.server_cipher is not None:
        expiry = self.server_cipher_age + rdfvalue.Duration('1d')
        if expiry > rdfvalue.RDFDatetime.Now():
            return self.server_cipher
    remote_public_key = self._GetRemotePublicKey(self.server_name)
    self.server_cipher = Cipher(self.common_name, self.private_key,
        remote_public_key)
    self.server_cipher_age = rdfvalue.RDFDatetime.Now()
    return self.server_cipher