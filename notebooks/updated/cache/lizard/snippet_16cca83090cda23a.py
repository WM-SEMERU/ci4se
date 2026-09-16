def create(self, name=None, description=None):
    uri = URITemplate(self.baseuri + '/{owner}').expand(owner=self.username)
    return self.session.post(uri, json=self._attribs(name, description))