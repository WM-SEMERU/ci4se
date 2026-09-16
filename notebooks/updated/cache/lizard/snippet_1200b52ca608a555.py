def decrypt(self, txt, key):
    assert isinstance(txt, six.text_type), 'txt: %s is not text type!' % repr(
        txt)
    assert isinstance(key, six.text_type), 'key: %s is not text type!' % repr(
        key)
    pbkdf2_hash, crypted = txt.rsplit('$', 1)
    try:
        crypted = binascii.unhexlify(crypted)
    except (binascii.Error, TypeError) as err:
        raise SecureJSLoginError('unhexlify error: %s with data: %s' % (err,
            crypted))
    if len(crypted) != len(key):
        raise SecureJSLoginError(
            "encrypt error: %s and '%s' must have the same length!" % (
            crypted, key))
    key = force_bytes(key)
    decrypted = self.xor(crypted, key)
    try:
        decrypted = force_text(decrypted)
    except UnicodeDecodeError:
        raise SecureJSLoginError("Can't decode data.")
    test = PBKDF2SHA1Hasher1().verify(decrypted, pbkdf2_hash)
    if not test:
        raise SecureJSLoginError('XOR decrypted data: PBKDF2 hash test failed')
    return decrypted