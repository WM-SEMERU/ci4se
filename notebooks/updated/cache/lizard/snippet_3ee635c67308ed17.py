def get_certificate_json(self, certificate_uid):
    if certificate_uid.startswith(URN_UUID_PREFIX):
        uid = certificate_uid[len(URN_UUID_PREFIX):]
    elif certificate_uid.startswith('http'):
        last_slash = certificate_uid.rindex('/')
        uid = certificate_uid[last_slash + 1:]
    else:
        uid = certificate_uid
    logging.debug('Retrieving certificate for uid=%s', uid)
    certificate_bytes = self._get_certificate_raw(uid)
    logging.debug('Found certificate for uid=%s', uid)
    certificate_json = helpers.certificate_bytes_to_json(certificate_bytes)
    return certificate_json