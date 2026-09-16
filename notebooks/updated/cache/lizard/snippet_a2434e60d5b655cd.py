def agent_key_info_from_key_id(key_id):
    if not FINGERPRINT_RE.match(key_id):
        ssh_key = load_ssh_key(key_id, True)
        fingerprint = ssh_key['fingerprint']
    else:
        fingerprint = key_id
    keys = Agent().get_keys()
    for key in keys:
        raw_key = key.blob
        md5_fp = fingerprint_from_raw_ssh_pub_key(raw_key)
        sha_fp = sha256_fingerprint_from_raw_ssh_pub_key(raw_key)
        if (sha_fp == fingerprint or md5_fp == fingerprint or 'MD5:' +
            md5_fp == fingerprint):
            md5_fingerprint = md5_fp
            break
    else:
        raise MantaError('no ssh-agent key with fingerprint "%s"' % fingerprint
            )
    return {'type': 'agent', 'agent_key': key, 'fingerprint':
        md5_fingerprint, 'algorithm': ALGO_FROM_SSH_KEY_TYPE[key.name]}