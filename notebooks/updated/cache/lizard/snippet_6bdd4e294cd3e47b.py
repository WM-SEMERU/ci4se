def reload(self):
    self._source = self._fetch_secrets(self._vault_url, self._path, self._token
        )