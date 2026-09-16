def List(self, listName, exclude_hidden_fields=False):
    return _List(self._session, listName, self._url, self._verify_ssl, self
        .users, self.huge_tree, self.timeout, exclude_hidden_fields=
        exclude_hidden_fields)