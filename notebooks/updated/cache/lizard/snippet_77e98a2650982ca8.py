def spread_stats(stats, spreader=False):
    spread = spread_t() if spreader else True
    descendants = deque(stats)
    while descendants:
        _stats = descendants.popleft()
        if spreader:
            spread.clear()
            yield _stats, spread
        else:
            yield _stats
        if spread:
            descendants.extend(_stats)