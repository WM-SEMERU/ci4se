def clear_url(self):
    if self.get_url_metadata().is_read_only() or self.get_url_metadata(
        ).is_required():
        raise errors.NoAccess()
    self._my_map['url'] = self._url_default