def compute_key(cli, familly, discriminant=None):
    hash_key = hashlib.sha256()
    hash_key.update(familly)
    hash_key.update(cli.host)
    hash_key.update(cli.user)
    hash_key.update(cli.password)
    if discriminant:
        if isinstance(discriminant, list):
            for i in discriminant:
                if i is not None and i is not False:
                    hash_key.update(str(i))
        elif isinstance(discriminant, tuple):
            for i in discriminant:
                if i is not None and i is not False:
                    hash_key.update(str(i))
        else:
            hash_key.update(discriminant)
    hash_key = hash_key.hexdigest()
    cli.log.debug('hash_key: ' + hash_key)
    return hash_key