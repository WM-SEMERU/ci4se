def retry(max_retries=1):

    def retry_func(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            num_retries = 0
            while num_retries <= max_retries:
                try:
                    ret = func(*args, **kwargs)
                    break
                except HTTPError:
                    if num_retries == max_retries:
                        raise
                    num_retries += 1
                    time.sleep(5)
            return ret
        return wrapper
    return retry_func