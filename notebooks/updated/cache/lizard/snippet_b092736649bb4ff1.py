def sleeping_func(arg, secs=10, result_queue=None):
    import time
    time.sleep(secs)
    if result_queue is not None:
        result_queue.put(arg)
    else:
        return arg