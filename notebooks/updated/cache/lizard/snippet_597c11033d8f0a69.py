def deserialize(self):
    if self.n and self.e:
        try:
            numbers = {}
            for param in self.longs:
                item = getattr(self, param)
                if not item:
                    continue
                else:
                    try:
                        val = int(deser(item))
                    except Exception:
                        raise
                    else:
                        numbers[param] = val
            if 'd' in numbers:
                self.priv_key = rsa_construct_private(numbers)
                self.pub_key = self.priv_key.public_key()
            else:
                self.pub_key = rsa_construct_public(numbers)
        except ValueError as err:
            raise DeSerializationNotPossible('%s' % err)
    if self.x5c:
        _cert_chain = []
        for der_data in self.x5c:
            _cert_chain.append(der_cert(base64.b64decode(der_data)))
        if self.x5t:
            if isinstance(self.x5t, bytes):
                _x5t = self.x5t
            else:
                _x5t = self.x5t.encode('ascii')
            if _x5t != x5t_calculation(self.x5c[0]):
                raise DeSerializationNotPossible(
                    "The thumbprint 'x5t' does not match the certificate.")
        if self.pub_key:
            if not rsa_eq(self.pub_key, _cert_chain[0].public_key()):
                raise ValueError(
                    'key described by components and key in x5c not equal')
        else:
            self.pub_key = _cert_chain[0].public_key()
        self._serialize(self.pub_key)
        if len(self.x5c) > 1:
            pass
    if not self.priv_key and not self.pub_key:
        raise DeSerializationNotPossible()