def delete(self, path):
    return self.session.delete(self._request_url(path), auth=self.auth,
        verify=False)