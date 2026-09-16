def import_keypair(self, keypair_name, key_material):
    query = self.query_factory(action='ImportKeyPair', creds=self.creds,
        endpoint=self.endpoint, other_params={'KeyName': keypair_name,
        'PublicKeyMaterial': b64encode(key_material)})
    d = query.submit()
    return d.addCallback(self.parser.import_keypair, key_material)