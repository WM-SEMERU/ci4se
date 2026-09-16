def member_data_for_in(self, leaderboard_name, member):
    return self.redis_connection.hget(self._member_data_key(
        leaderboard_name), member)