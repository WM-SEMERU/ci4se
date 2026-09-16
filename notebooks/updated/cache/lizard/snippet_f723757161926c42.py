def update_member_data_in(self, leaderboard_name, member, member_data):
    self.redis_connection.hset(self._member_data_key(leaderboard_name),
        member, member_data)