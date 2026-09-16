def update(self):
    if not self.can_update():
        self._tcex.handle_error(905, [self.type])
    return self.tc_requests.update(self.api_type, self.api_sub_type, self.
        unique_id, self._data, owner=self.owner)