def export_public_key(vk, label):
    key_type, blob = serialize_verifying_key(vk)
    log.debug('fingerprint: %s', fingerprint(blob))
    b64 = base64.b64encode(blob).decode('ascii')
    return '{} {} {}\n'.format(key_type.decode('ascii'), b64, label)