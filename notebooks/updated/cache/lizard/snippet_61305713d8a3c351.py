def rate_limit(client, headers, atexit=False):
    if not client or not headers:
        return False
    if not getattr(client.config, 'rate_limit', False):
        return False
    rate_info = RateLimitsInfo.from_headers(headers)
    if not rate_info or not rate_info.interval:
        return False
    if rate_info.interval:
        cb = getattr(client.config, 'rate_limit_callback', None)
        if cb and callable(cb):
            cb(rate_info, atexit=atexit)
        time.sleep(rate_info.interval)
    return True