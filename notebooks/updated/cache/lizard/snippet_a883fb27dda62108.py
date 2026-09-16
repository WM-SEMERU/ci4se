def prune_cached(values):
    import os
    config_path = os.path.expanduser('~/.config/blockade')
    file_path = os.path.join(config_path, 'cache.txt')
    if not os.path.isfile(file_path):
        return values
    cached = [x.strip() for x in open(file_path, 'r').readlines()]
    output = list()
    for item in values:
        hashed = hash_values(item)
        if hashed in cached:
            continue
        output.append(item)
    return output