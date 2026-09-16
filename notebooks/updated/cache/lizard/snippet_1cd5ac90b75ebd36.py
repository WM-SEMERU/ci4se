def sign(self, message):
    return hmac.HMAC(self.key, message, digestmod=hashlib.md5).digest()