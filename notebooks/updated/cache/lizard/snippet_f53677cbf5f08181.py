def transfer_extensions_for_identities(self, identity_mapping):
    content = self._serialize.body(identity_mapping, '[IdentityMapping]')
    self._send(http_method='POST', location_id=
        'da46fe26-dbb6-41d9-9d6b-86bf47e4e444', version='5.1-preview.1',
        content=content)