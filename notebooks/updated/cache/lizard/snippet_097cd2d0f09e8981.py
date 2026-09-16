def set(self, id, translation, domain='messages'):
    assert isinstance(id, (str, unicode))
    assert isinstance(translation, (str, unicode))
    assert isinstance(domain, (str, unicode))
    self.add({id: translation}, domain)