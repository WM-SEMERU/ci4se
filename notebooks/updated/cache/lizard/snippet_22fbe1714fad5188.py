def PwCrypt(self, password):
    if self.authenticator is None:
        self.authenticator = self.CreateAuthenticator()
    if isinstance(password, six.text_type):
        password = password.encode('utf-8')
    buf = password
    if len(password) % 16 != 0:
        buf += six.b('\x00') * (16 - len(password) % 16)
    hash = md5_constructor(self.secret + self.authenticator).digest()
    result = six.b('')
    last = self.authenticator
    while buf:
        hash = md5_constructor(self.secret + last).digest()
        if six.PY3:
            for i in range(16):
                result += bytes((hash[i] ^ buf[i],))
        else:
            for i in range(16):
                result += chr(ord(hash[i]) ^ ord(buf[i]))
        last = result[-16:]
        buf = buf[16:]
    return result