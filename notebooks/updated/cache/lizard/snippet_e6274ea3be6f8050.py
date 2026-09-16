def get_next_seed(key, seed):
    return hmac.new(key, seed, hashlib.sha256).digest()