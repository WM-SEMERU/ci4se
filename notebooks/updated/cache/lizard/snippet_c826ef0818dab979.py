def permanently_delete(self, user):
    url = self._build_url(self.endpoint.deleted(id=user))
    deleted_user = self._delete(url)
    self.cache.delete(deleted_user)
    return deleted_user