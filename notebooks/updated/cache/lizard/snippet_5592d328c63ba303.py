def parse_digest_challenge(authentication_header):
    if not is_digest_challenge(authentication_header):
        return None
    parts = parse_parts(authentication_header[7:], defaults={'algorithm':
        'MD5', 'stale': 'false'})
    if not _check_required_parts(parts, _REQUIRED_DIGEST_CHALLENGE_PARTS):
        return None
    parts['stale'] = parts['stale'].lower() == 'true'
    digest_challenge = _build_object_from_parts(parts,
        _REQUIRED_DIGEST_CHALLENGE_PARTS)
    if ('MD5', 'auth') != (digest_challenge.algorithm, digest_challenge.qop):
        return None
    return digest_challenge