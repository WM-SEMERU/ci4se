def download(self):
    if not self.can_update():
        self._tcex.handle_error(910, [self.type])
    return self.tc_requests.download(self.api_type, self.api_sub_type, self
        .unique_id)