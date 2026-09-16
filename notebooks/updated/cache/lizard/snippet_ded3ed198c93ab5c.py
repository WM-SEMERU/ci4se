def clear_created_date(self):
    if self.get_created_date_metadata().is_read_only(
        ) or self.get_created_date_metadata().is_required():
        raise errors.NoAccess()
    self._my_map['createdDate'] = self._created_date_default