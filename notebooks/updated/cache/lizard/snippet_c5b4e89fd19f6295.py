def uuid(self, **params):
    digest = str(uuidlib.uuid4()).replace('-', '')
    return self.humanize(digest, **params), digest