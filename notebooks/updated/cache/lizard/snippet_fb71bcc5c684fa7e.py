def get_relationships(self):
    url_path = ('/handcar/services/relationship/families/' + self.
        _catalog_idstr + '/relationships')
    return objects.RelationshipList(self._get_request(url_path))