def aes_kdf(key, rounds, password=None, keyfile=None):
    cipher = AES.new(key, AES.MODE_ECB)
    key_composite = compute_key_composite(password=password, keyfile=keyfile)
    transformed_key = key_composite
    for _ in range(0, rounds):
        transformed_key = cipher.encrypt(transformed_key)
    return hashlib.sha256(transformed_key).digest()