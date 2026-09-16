def get_body_hash(params):
    norm_params = get_normalized_params(params)
    return binascii.b2a_base64(hashlib.sha1(norm_params).digest())[:-1]