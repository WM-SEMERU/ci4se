def clear_end_date(self):
    if self.get_end_date_metadata().is_read_only(
        ) or self.get_end_date_metadata().is_required():
        raise errors.NoAccess()
    self._my_map['endDate'] = self._mdata['end_date'][
        'default_date_time_values'][0]