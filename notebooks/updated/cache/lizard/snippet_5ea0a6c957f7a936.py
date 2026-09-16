def _decode(hashid, salt, alphabet, separators, guards):
    parts = tuple(_split(hashid, guards))
    hashid = parts[1] if 2 <= len(parts) <= 3 else parts[0]
    if not hashid:
        return
    lottery_char = hashid[0]
    hashid = hashid[1:]
    hash_parts = _split(hashid, separators)
    for part in hash_parts:
        alphabet_salt = (lottery_char + salt + alphabet)[:len(alphabet)]
        alphabet = _reorder(alphabet, alphabet_salt)
        yield _unhash(part, alphabet)