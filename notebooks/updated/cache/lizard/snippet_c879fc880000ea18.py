def generate_ed25519_key(scheme='ed25519'):
    securesystemslib.formats.ED25519_SIG_SCHEMA.check_match(scheme)
    ed25519_key = {}
    keytype = 'ed25519'
    public = None
    private = None
    public, private = (securesystemslib.ed25519_keys.
        generate_public_and_private())
    key_value = {'public': binascii.hexlify(public).decode(), 'private': ''}
    keyid = _get_keyid(keytype, scheme, key_value)
    key_value['private'] = binascii.hexlify(private).decode()
    ed25519_key['keytype'] = keytype
    ed25519_key['scheme'] = scheme
    ed25519_key['keyid'] = keyid
    ed25519_key['keyid_hash_algorithms'
        ] = securesystemslib.settings.HASH_ALGORITHMS
    ed25519_key['keyval'] = key_value
    return ed25519_key