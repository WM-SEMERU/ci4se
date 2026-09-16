def fingerprint(self):
    if self._fingerprint is None:
        params = self['private_key_algorithm']['parameters']
        key = self['private_key'].parsed
        if self.algorithm == 'rsa':
            to_hash = '%d:%d' % (key['modulus'].native, key[
                'public_exponent'].native)
        elif self.algorithm == 'dsa':
            public_key = self.public_key
            to_hash = '%d:%d:%d:%d' % (params['p'].native, params['q'].
                native, params['g'].native, public_key.native)
        elif self.algorithm == 'ec':
            public_key = key['public_key'].native
            if public_key is None:
                public_key = self.public_key.native
            if params.name == 'named':
                to_hash = '%s:' % params.chosen.native
                to_hash = to_hash.encode('utf-8')
                to_hash += public_key
            elif params.name == 'implicit_ca':
                to_hash = public_key
            elif params.name == 'specified':
                to_hash = '%s:' % params.chosen['field_id']['parameters'
                    ].native
                to_hash = to_hash.encode('utf-8')
                to_hash += b':' + params.chosen['curve']['a'].native
                to_hash += b':' + params.chosen['curve']['b'].native
                to_hash += public_key
        if isinstance(to_hash, str_cls):
            to_hash = to_hash.encode('utf-8')
        self._fingerprint = hashlib.sha256(to_hash).digest()
    return self._fingerprint