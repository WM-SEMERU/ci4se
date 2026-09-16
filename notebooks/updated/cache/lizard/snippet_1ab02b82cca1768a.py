def expire_leaderboard_at_for(self, leaderboard_name, timestamp):
    pipeline = self.redis_connection.pipeline()
    pipeline.expireat(leaderboard_name, timestamp)
    pipeline.expireat(self._ties_leaderboard_key(leaderboard_name), timestamp)
    pipeline.expireat(self._member_data_key(leaderboard_name), timestamp)
    pipeline.execute()