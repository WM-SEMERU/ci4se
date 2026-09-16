def sign_message(privkey_path, message, passphrase=None):
    key = get_rsa_key(privkey_path, passphrase)
    log.debug('salt.crypt.sign_message: Signing message.')
    if HAS_M2:
        md = EVP.MessageDigest('sha1')
        md.update(salt.utils.stringutils.to_bytes(message))
        digest = md.final()
        return key.sign(digest)
    else:
        signer = PKCS1_v1_5.new(key)
        return signer.sign(SHA.new(salt.utils.stringutils.to_bytes(message)))