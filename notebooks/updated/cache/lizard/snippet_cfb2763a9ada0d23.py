def clear_provider(self):
    if self.get_provider_metadata().is_read_only(
        ) or self.get_provider_metadata().is_required():
        raise errors.NoAccess()
    self._my_map['providerId'] = self._provider_default