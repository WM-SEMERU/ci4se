def set_provider(self, provider_id):
    if self.get_provider_metadata().is_read_only():
        raise errors.NoAccess()
    if not self._is_valid_id(provider_id):
        raise errors.InvalidArgument()
    self._my_map['providerId'] = str(provider_id)