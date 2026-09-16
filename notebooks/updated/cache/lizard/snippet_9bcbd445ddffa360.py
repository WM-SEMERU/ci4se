def ISINSTANCE(instance, A_tuple):
    try:
        instance = instance._redpipe_future_result
    except AttributeError:
        pass
    return isinstance(instance, A_tuple)