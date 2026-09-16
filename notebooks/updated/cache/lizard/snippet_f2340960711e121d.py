def unsign(self, token):
    if self.max_age is None:
        data = self.signer.unsign(token)
    else:
        data = self.signer.unsign(token, max_age=self.max_age)
    return signing.b64_decode(data.encode())