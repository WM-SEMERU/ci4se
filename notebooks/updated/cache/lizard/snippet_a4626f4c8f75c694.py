def score_for_in(self, leaderboard_name, member):
    score = self.redis_connection.zscore(leaderboard_name, member)
    if score is not None:
        score = float(score)
    return score