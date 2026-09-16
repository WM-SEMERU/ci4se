def make_private(self, client=None):
    self.acl.all().revoke_read()
    self.acl.save(client=client)