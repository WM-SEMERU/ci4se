def leaderboard(self):
    if self._leaderboard is None:
        self.assert_bind_client()
        if self.id is not None:
            self._leaderboard = self.bind_client.get_segment_leaderboard(self
                .id)
    return self._leaderboard