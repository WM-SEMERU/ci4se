def indicate_last(items):
    last_index = len(items) - 1
    for i, item in enumerate(items):
        yield i == last_index, item