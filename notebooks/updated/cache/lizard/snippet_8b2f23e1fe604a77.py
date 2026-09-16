def add_play(self, choice, count=1):
    self.redis.hincrby(EXPERIMENT_REDIS_KEY_TEMPLATE % self.name, 
        '%s:plays' % choice, count)
    self._choices = None