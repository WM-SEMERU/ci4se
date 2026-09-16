def create_key_pair(self, key_name):
    params = {'KeyName': key_name}
    return self.get_object('CreateKeyPair', params, KeyPair, verb='POST')