def _check_preferences(prefs, pref_type=None):
    if prefs is None:
        return
    cipher = frozenset(['AES256', 'AES192', 'AES128', 'CAMELLIA256',
        'CAMELLIA192', 'TWOFISH', '3DES'])
    digest = frozenset(['SHA512', 'SHA384', 'SHA256', 'SHA224', 'RMD160',
        'SHA1'])
    compress = frozenset(['BZIP2', 'ZLIB', 'ZIP', 'Uncompressed'])
    trust = frozenset(['gpg', 'classic', 'direct', 'always', 'auto'])
    pinentry = frozenset(['loopback'])
    all = frozenset([cipher, digest, compress, trust, pinentry])
    if isinstance(prefs, str):
        prefs = set(prefs.split())
    elif isinstance(prefs, list):
        prefs = set(prefs)
    else:
        msg = 'prefs must be list of strings, or space-separated string'
        log.error('parsers._check_preferences(): %s' % message)
        raise TypeError(message)
    if not pref_type:
        pref_type = 'all'
    allowed = str()
    if pref_type == 'cipher':
        allowed += ' '.join(prefs.intersection(cipher))
    if pref_type == 'digest':
        allowed += ' '.join(prefs.intersection(digest))
    if pref_type == 'compress':
        allowed += ' '.join(prefs.intersection(compress))
    if pref_type == 'trust':
        allowed += ' '.join(prefs.intersection(trust))
    if pref_type == 'pinentry':
        allowed += ' '.join(prefs.intersection(pinentry))
    if pref_type == 'all':
        allowed += ' '.join(prefs.intersection(all))
    return allowed