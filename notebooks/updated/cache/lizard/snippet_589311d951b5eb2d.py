def compute_ecc_hash(ecc_manager, hasher, buf, max_block_size, rate,
    message_size=None, as_string=False):
    result = []
    if not message_size:
        ecc_params = compute_ecc_params(max_block_size, rate, hasher)
        message_size = ecc_params['message_size']
    for i in xrange(0, len(buf), message_size):
        mes = buf[i:i + message_size]
        ecc = ecc_manager.encode(mes)
        hash = hasher.hash(mes)
        if as_string:
            result.append('%s%s' % (str(hash), str(ecc)))
        else:
            result.append([hash, ecc])
    return result