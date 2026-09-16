def get_collaborator_permission(self, collaborator):
    assert isinstance(collaborator, github.NamedUser.NamedUser) or isinstance(
        collaborator, (str, unicode)), collaborator
    if isinstance(collaborator, github.NamedUser.NamedUser):
        collaborator = collaborator._identity
    headers, data = self._requester.requestJsonAndCheck('GET', self.url +
        '/collaborators/' + collaborator + '/permission')
    return data['permission']