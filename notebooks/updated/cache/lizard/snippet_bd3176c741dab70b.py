def total_members_in_score_range_in(self, leaderboard_name, min_score,
    max_score):
    return self.redis_connection.zcount(leaderboard_name, min_score, max_score)