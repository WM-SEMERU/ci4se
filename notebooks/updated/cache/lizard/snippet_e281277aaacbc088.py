def retry_bool(callback, times=3, cap=120000):
    for attempt in range(times + 1):
        if attempt > 0:
            time.sleep(retry_wait_time(attempt, cap) / 1000.0)
        ret = callback()
        if ret or attempt == times:
            break
    return ret