def scheduled_jobs(with_times=False, connection=None):
    if connection is None:
        connection = r
    jobs = connection.zrangebyscore(REDIS_KEY, 0, sys.maxsize, withscores=
        with_times)
    for job in jobs:
        if with_times:
            yield job[0].decode('utf-8'), job[1]
        else:
            yield job.decode('utf-8')