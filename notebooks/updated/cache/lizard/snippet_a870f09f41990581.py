def sort_by_priority(iterable, reverse=False, default_priority=10):
    return sorted(iterable, reverse=reverse, key=lambda o: getattr(o,
        'priority', default_priority))