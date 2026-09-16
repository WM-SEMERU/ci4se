def wait_for(func):

    def wrapped(*args, **kwargs):
        timeout = kwargs.pop('timeout', 15)
        start = time()
        result = None
        while time() - start < timeout:
            result = func(*args, **kwargs)
            if result:
                break
            sleep(0.2)
        return result
    return wrapped