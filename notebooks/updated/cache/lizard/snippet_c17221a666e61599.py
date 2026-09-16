def add_observers(self, count, date_observed):
    if not self.can_update():
        self._tcex.handle_error(910, [self.type])
    data = {'count': count, 'dataObserved': self._utils.format_datetime(
        date_observed, date_format='%Y-%m-%dT%H:%M:%SZ')}
    return self.tc_requests.add_observations(self.api_type, self.
        api_sub_type, self.unique_id, data, owner=self.owner)