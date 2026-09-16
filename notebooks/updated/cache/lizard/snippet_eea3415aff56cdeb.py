def nonce(algorithm='sha1', to_hex=True):
    if algorithm not in _HASHES:
        return None
    result = _HASHES[algorithm](datetime.datetime.now().isoformat())
    return result.hexdigest() if to_hex else b64encode(result.digest())