def fixed_interval_scheduler(interval):
    start = time.time()
    next_tick = start
    while True:
        next_tick += interval
        yield next_tick