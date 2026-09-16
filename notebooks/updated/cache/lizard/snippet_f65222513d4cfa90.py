def check_secret(self, secret):
    try:
        return hmac.compare_digest(secret, self.secret)
    except AttributeError:
        return secret == self.secret