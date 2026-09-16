def init(cls, redis_host: str, redis_port: int, is_sentinel_redis=False,
    redis_sentinel_service='mymaster', redis_password=None):
    if not cls.redis_helper:
        cls.redis_helper = RedisHelper(host=redis_host, port=redis_port,
            is_sentinel=is_sentinel_redis, sentinel_service=
            redis_sentinel_service, password=redis_password)