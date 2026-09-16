def _hash(self, iv, value):
    return hmac.new(self.key, msg=iv + value, digestmod=hashlib.sha256
        ).hexdigest()