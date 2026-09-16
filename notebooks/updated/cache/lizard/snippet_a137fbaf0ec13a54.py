def mgf1(mgf_seed, mask_len, hash_class=hashlib.sha1):
    h_len = hash_class().digest_size
    if mask_len > 65536:
        raise ValueError('mask too long')
    T = b''
    for i in range(0, integer_ceil(mask_len, h_len)):
        C = i2osp(i, 4)
        T = T + hash_class(mgf_seed + C).digest()
    return T[:mask_len]