def assignees(self):
    if not self.can_update():
        self._tcex.handle_error(910, [self.type])
    for a in self.tc_requests.assignees(self.api_type, self.api_sub_type,
        self.unique_id):
        yield a