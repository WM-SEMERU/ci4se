def _openssl_key_iv(passphrase, salt):

    def _openssl_kdf(req):
        if hasattr(passphrase, 'encode'):
            passwd = passphrase.encode('ascii', 'ignore')
        else:
            passwd = passphrase
        prev = b''
        while req > 0:
            digest = hashes.Hash(hashes.MD5(), backend=default_backend())
            digest.update(prev + passwd + salt)
            prev = digest.finalize()
            req -= IV_BLOCK_SIZE
            yield prev
    assert passphrase is not None
    assert salt is not None
    mat = b''.join([x for x in _openssl_kdf(32 + IV_BLOCK_SIZE)])
    return mat[0:32], mat[32:32 + IV_BLOCK_SIZE]