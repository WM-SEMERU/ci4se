def clear_priority(self):
    if self.get_priority_metadata().is_read_only(
        ) or self.get_priority_metadata().is_required():
        raise errors.NoAccess()
    self._my_map['priority'] = self._priority_default