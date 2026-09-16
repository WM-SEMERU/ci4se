def increment_score(self, member, amount=1):
    return self.redis.zincrby(self.key, float(amount), self._pickle(member))