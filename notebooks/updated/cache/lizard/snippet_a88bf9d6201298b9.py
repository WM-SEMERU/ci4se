def calculate_hash(options):
    options = sorted(list(options))
    sha_hash = sha1()
    sha_hash.update(''.join(options).encode('utf-8'))
    return sha_hash.hexdigest()