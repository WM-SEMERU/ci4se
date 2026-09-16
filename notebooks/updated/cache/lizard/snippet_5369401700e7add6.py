def _exponential_timeout_generator(initial, maximum, multiplier, deadline):
    if deadline is not None:
        deadline_datetime = datetime_helpers.utcnow() + datetime.timedelta(
            seconds=deadline)
    else:
        deadline_datetime = datetime.datetime.max
    timeout = initial
    while True:
        now = datetime_helpers.utcnow()
        yield min(timeout, maximum, float((deadline_datetime - now).seconds))
        timeout = timeout * multiplier