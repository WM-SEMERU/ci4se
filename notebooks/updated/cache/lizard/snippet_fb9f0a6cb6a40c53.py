def sha256_fingerprint_from_raw_ssh_pub_key(raw_key):
    digest = hashlib.sha256(raw_key).digest()
    h = base64.b64encode(digest).decode('utf-8')
    h = h.rstrip().rstrip('=')
    return 'SHA256:' + h