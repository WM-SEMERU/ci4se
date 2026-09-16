def path_deserialize(cls, serialized_path):

    def _chomp_netstring_payload(s):
        try:
            ns_len_str, ns_body = s.split(':', 1)
            ns_len = int(ns_len_str)
            assert ns_body[ns_len] == ','
            ns_payload = ns_body[:ns_len]
            return ns_payload, ns_body[ns_len + 1:]
        except:
            raise ValueError("Invalid netstring '{}'".format(s))
    path_str, extra = _chomp_netstring_payload(serialized_path)
    if len(extra) > 0:
        raise ValueError("Danlging data in '{}'".format(serialized_path))
    path = []
    while True:
        path_part, path_str = _chomp_netstring_payload(path_str)
        try:
            order, hash_hex = path_part.split('-', 1)
            assert order in ['l', 'r', 'm']
            path.append({'order': order, 'hash': hash_hex})
        except:
            raise ValueError('Invalid path entry {}'.format(path_part))
        if len(path_str) == 0:
            break
    return path