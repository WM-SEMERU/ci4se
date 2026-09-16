def delete_key(keyid=None, fingerprint=None, delete_secret=False, user=None,
    gnupghome=None):
    ret = {'res': True, 'message': ''}
    if fingerprint and keyid:
        ret['res'] = False
        ret['message'] = 'Only specify one argument, fingerprint or keyid'
        return ret
    if not fingerprint and not keyid:
        ret['res'] = False
        ret['message'] = 'Required argument, fingerprint or keyid'
        return ret
    gpg = _create_gpg(user, gnupghome)
    key = get_key(keyid, fingerprint, user)
    if key:
        fingerprint = key['fingerprint']
        skey = get_secret_key(keyid, fingerprint, user)
        if skey and not delete_secret:
            ret['res'] = False
            ret['message'
                ] = 'Secret key exists, delete first or pass delete_secret=True.'
            return ret
        elif skey and delete_secret and six.text_type(gpg.delete_keys(
            fingerprint, True)) == 'ok':
            ret['message'] = 'Secret key for {0} deleted\n'.format(fingerprint)
        if six.text_type(gpg.delete_keys(fingerprint)) == 'ok':
            ret['message'] += 'Public key for {0} deleted'.format(fingerprint)
        ret['res'] = True
        return ret
    else:
        ret['res'] = False
        ret['message'] = 'Key not available in keychain.'
        return ret