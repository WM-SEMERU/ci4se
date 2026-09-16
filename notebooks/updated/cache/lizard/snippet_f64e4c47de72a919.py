def verify_signature(self, signature, nonce, timestamp, signed_id):
    message = '%s%s%s%s' % (self.api_key, nonce, timestamp, signed_id)
    if self._pub_key is None:
        warnings.warn(
            'Skipping RSA signature verification. Please pass public key on class initialization to ensure highest level of security!'
            )
        return True
    try:
        rsa.verify(message.encode('utf-8'), signature, self._pub_key)
    except rsa.VerificationError:
        return False
    return True