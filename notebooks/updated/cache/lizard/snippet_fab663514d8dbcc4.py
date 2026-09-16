def iter_window(iterable, size=2, step=1, wrap=False):
    r
    iter_list = it.tee(iterable, size)
    if wrap:
        iter_list = [iter_list[0]] + list(map(it.cycle, iter_list[1:]))
    try:
        for count, iter_ in enumerate(iter_list[1:], start=1):
            for _ in range(count):
                six.next(iter_)
    except StopIteration:
        return iter(())
    else:
        _window_iter = zip(*iter_list)
        window_iter = it.islice(_window_iter, 0, None, step)
        return window_iter