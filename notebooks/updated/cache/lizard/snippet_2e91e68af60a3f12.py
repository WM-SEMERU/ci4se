def _validate_claim_request(claims, ignore_errors=False):
    results = {}
    claims = claims if claims else {}
    for name, value in claims.iteritems():
        if value is None:
            results[name] = None
        elif isinstance(value, dict):
            results[name] = _validate_claim_values(name, value, ignore_errors)
        elif not ignore_errors:
            msg = 'Invalid claim {}.'.format(name)
            raise ValueError(msg)
    return results