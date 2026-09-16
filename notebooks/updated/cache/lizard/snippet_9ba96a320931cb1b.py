def remove_outside_collaborator(self, collaborator):
    assert isinstance(collaborator, github.NamedUser.NamedUser), collaborator
    headers, data = self._requester.requestJsonAndCheck('DELETE', self.url +
        '/outside_collaborators/' + collaborator._identity)