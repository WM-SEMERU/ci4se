def remove_member_from(self, leaderboard_name, member):
    pipeline = self.redis_connection.pipeline()
    pipeline.zrem(leaderboard_name, member)
    pipeline.hdel(self._member_data_key(leaderboard_name), member)
    pipeline.execute()