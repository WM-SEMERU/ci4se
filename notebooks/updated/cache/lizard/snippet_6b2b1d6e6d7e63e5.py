def retrier(*, max_attempts, sleeptime, max_sleeptime, sleepscale=1.5,
    jitter=0.2):
    assert max_attempts > 1
    assert sleeptime >= 0
    assert 0 <= jitter <= sleeptime
    assert sleepscale >= 1
    cur_sleeptime = min(max_sleeptime, sleeptime)
    for attempt in range(max_attempts):
        cur_jitter = random.randint(int(-jitter * 1000), int(jitter * 1000)
            ) / 1000
        yield max(0, cur_sleeptime + cur_jitter)
        cur_sleeptime = min(max_sleeptime, cur_sleeptime * sleepscale)