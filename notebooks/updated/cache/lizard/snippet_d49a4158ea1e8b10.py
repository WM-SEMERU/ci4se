def encrypt(self, recipient_id, message):
    logger.debug('encrypt(recipientid=%s, message=%s)' % (recipient_id,
        message))
    cipher = self._get_session_cipher(recipient_id)
    return cipher.encrypt(message + self._generate_random_padding())