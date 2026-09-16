def to_ipv6(key):
    if key[-2:] != '.k':
        raise ValueError('Key does not end with .k')
    key_bytes = base32.decode(key[:-2])
    hash_one = sha512(key_bytes).digest()
    hash_two = sha512(hash_one).hexdigest()
    return ':'.join([hash_two[i:i + 4] for i in range(0, 32, 4)])