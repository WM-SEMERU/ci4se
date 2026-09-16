def per_delta(start: datetime, end: datetime, delta: timedelta):
    curr = start
    while curr < end:
        curr_end = curr + delta
        yield curr, curr_end
        curr = curr_end