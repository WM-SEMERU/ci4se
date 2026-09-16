def remove_by_rank(self, low, high=None):
    if high is None:
        high = low
    return self.database.zremrangebyrank(self.key, low, high)