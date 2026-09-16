def remove_member_from(self, leaderboard_name, member):
    member_score = None or self.redis_connection.zscore(leaderboard_name,
        member)
    can_delete_score = member_score and len(self.
        members_from_score_range_in(leaderboard_name, member_score,
        member_score)) == 1
    pipeline = self.redis_connection.pipeline()
    pipeline.zrem(leaderboard_name, member)
    if can_delete_score:
        pipeline.zrem(self._ties_leaderboard_key(leaderboard_name), str(
            float(member_score)))
    pipeline.hdel(self._member_data_key(leaderboard_name), member)
    pipeline.execute()