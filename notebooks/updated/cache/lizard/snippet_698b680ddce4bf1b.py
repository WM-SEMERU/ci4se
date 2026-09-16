def ToJson(self):
    jsn = super(EnrollmentTransaction, self).ToJson()
    jsn['pubkey'] = self.PublicKey.ToString()
    return jsn