def call_interval(freq, **kwargs):

    def wrapper(f):
        return CallInterval(f, freq, **kwargs)
    return wrapper