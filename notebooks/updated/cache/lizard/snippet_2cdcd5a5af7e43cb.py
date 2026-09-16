def add_client_to_manifest(self, client_id, client_secret, manifest):
    assert self.is_admin, 'Must authenticate() as admin to create client'
    return self.uaac.add_client_to_manifest(client_id, client_secret, manifest)