def compute_authenticator(self, packed_request_auth, shared_secret):
    data = prepare_packed_data(self, packed_request_auth)
    radius_mac = hashlib.md5(data + shared_secret)
    return radius_mac.digest()