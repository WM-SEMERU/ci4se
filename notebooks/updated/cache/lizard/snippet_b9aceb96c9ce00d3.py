def set_system_lock(cls, redis, name, timeout):
    pipeline = redis.pipeline()
    pipeline.zadd(name, SYSTEM_LOCK_ID, time.time() + timeout)
    pipeline.expire(name, timeout + 10)
    pipeline.execute()