def redis(self):
    if self._redis is None:
        self._redis = redis.StrictRedis(host=self.args.redis_host, port=
            self.args.redis_port)
    return self._redis