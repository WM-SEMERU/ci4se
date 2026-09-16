def encode_w_salt(self, salt, key):
    enc_key = '%s%s' % (salt, key)
    enc_val = hashlib.sha1(enc_key).hexdigest()
    return 'sha1:%s$%s' % (salt, enc_val)