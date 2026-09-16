def archive(self):
    pipe = self.redis.pipeline(transaction=True)
    pipe.srem(ACTIVE_EXPERIMENTS_REDIS_KEY, self.name)
    pipe.sadd(ARCHIVED_EXPERIMENTS_REDIS_KEY, self.name)
    pipe.execute()