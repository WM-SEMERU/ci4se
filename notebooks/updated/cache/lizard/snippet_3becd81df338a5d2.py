def _wait(starting_time, first_timestamp, timestamp):
    target_time = starting_time + (timestamp - first_timestamp)
    time.sleep(max(target_time - time.time(), 0))