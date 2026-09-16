def hash_key(self):
    if self.conf.message_id:
        message_id = self.message.get('Message-Id')
        if message_id:
            return message_id.strip()
        logger.error('No Message-ID in {}: {}'.format(self.path, self.
            header_text))
        raise MissingMessageID
    return hashlib.sha224(self.canonical_headers).hexdigest()