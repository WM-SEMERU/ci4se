def reminder_date(self, reminder_date):
    if not self.can_update():
        self._tcex.handle_error(910, [self.type])
    reminder_date = self._utils.format_datetime(reminder_date, date_format=
        '%Y-%m-%dT%H:%M:%SZ')
    self._data['reminderDate'] = reminder_date
    request = {'reminderDate': reminder_date}
    return self.tc_requests.update(self.api_type, self.api_sub_type, self.
        unique_id, request)