def members(self):
    if self._members is None:
        self.assert_bind_client()
        self._members = self.bind_client.get_club_members(self.id)
    return self._members