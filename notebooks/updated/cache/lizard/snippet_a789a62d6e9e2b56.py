def get_rate_limits(response):
    periods = response.headers['X-RateLimit-Period']
    if not periods:
        return []
    rate_limits = []
    periods = periods.split(',')
    limits = response.headers['X-RateLimit-Limit'].split(',')
    remaining = response.headers['X-RateLimit-Remaining'].split(',')
    reset = response.headers['X-RateLimit-Reset'].split(',')
    for idx, period in enumerate(periods):
        rate_limit = {}
        limit_period = get_readable_time_string(period)
        rate_limit['period'] = limit_period
        rate_limit['period_seconds'] = period
        rate_limit['request_limit'] = limits[idx]
        rate_limit['requests_remaining'] = remaining[idx]
        reset_datetime = get_datetime_from_timestamp(reset[idx])
        rate_limit['reset'] = reset_datetime
        right_now = datetime.now()
        if reset_datetime is not None and right_now < reset_datetime:
            seconds_remaining = (reset_datetime - right_now).seconds + 1
        else:
            seconds_remaining = 0
        rate_limit['reset_in_seconds'] = seconds_remaining
        rate_limit['time_to_reset'] = get_readable_time_string(
            seconds_remaining)
        rate_limits.append(rate_limit)
    return rate_limits