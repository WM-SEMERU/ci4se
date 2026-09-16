def get_identities(self, item):
    identities = []
    field = self.get_field_author()
    identities.append(self.get_sh_identity(item, field))
    return identities