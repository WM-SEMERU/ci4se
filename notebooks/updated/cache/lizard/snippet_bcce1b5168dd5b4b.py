def intersect_leaderboards(self, destination, keys, aggregate='SUM'):
    keys.insert(0, self.leaderboard_name)
    self.redis_connection.zinterstore(destination, keys, aggregate)