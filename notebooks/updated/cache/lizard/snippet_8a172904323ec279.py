def get_identities(self, item):
    identities = []
    if 'data' not in item:
        return identities
    if 'revisions' not in item['data']:
        return identities
    revisions = item['data']['revisions']
    for revision in revisions:
        user = self.get_sh_identity(revision)
        yield user