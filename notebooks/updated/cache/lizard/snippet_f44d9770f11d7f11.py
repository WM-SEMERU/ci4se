def as_completed(*async_result_wrappers):
    for item in async_result_wrappers:
        if not isinstance(item, AsyncMethodCall):
            raise TypeError('Got non-AsyncMethodCall object: {}'.format(item))
    wrappers_copy = list(async_result_wrappers)
    while len(wrappers_copy):
        completed = list(filter(lambda x: x.finished(), wrappers_copy))
        if not len(completed):
            continue
        for item in completed:
            wrappers_copy.remove(item)
            yield item