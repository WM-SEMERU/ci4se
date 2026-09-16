def transform_sequence(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        return lambda seq: seq.map_points(partial(f, *args, **kwargs))
    return wrapper