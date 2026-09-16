def get_mac_signature(api_secret, norm_request_string):
    hashed = hmac.new(str(api_secret), norm_request_string, hashlib.sha1)
    return binascii.b2a_base64(hashed.digest())[:-1]