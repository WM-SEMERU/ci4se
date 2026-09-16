def private_key(self, s):
    s = parseable_str(s)
    for f in [self.wif, self.secret_exponent]:
        v = f(s)
        if v:
            return v