def timer(name, reservoir_type='uniform', *reservoir_args, **reservoir_kwargs):
    hmetric = get_or_create_histogram(name, reservoir_type, *reservoir_args,
        **reservoir_kwargs)
    t1 = time.time()
    yield
    t2 = time.time()
    hmetric.notify(t2 - t1)