def verify_signature(pubkey_path, message, signature):
    log.debug('salt.crypt.verify_signature: Loading public key')
    pubkey = get_rsa_pub_key(pubkey_path)
    log.debug('salt.crypt.verify_signature: Verifying signature')
    if HAS_M2:
        md = EVP.MessageDigest('sha1')
        md.update(salt.utils.stringutils.to_bytes(message))
        digest = md.final()
        return pubkey.verify(digest, signature)
    else:
        verifier = PKCS1_v1_5.new(pubkey)
        return verifier.verify(SHA.new(salt.utils.stringutils.to_bytes(
            message)), signature)