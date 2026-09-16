def dynamic_sum(values, limit_n=1000, acc=0, depth=4):
    if len(values) < limit_n:
        return acc + sum(values)
    if depth > 0:
        half = len(values) // 2
        return add(dynamic_sum(values[:half], limit_n, acc, depth=depth - 1
            ), dynamic_sum(values[half:], limit_n, 0, depth=depth - 1))
    return dynamic_sum(values[limit_n:], limit_n, acc + sum(values[:limit_n
        ]), depth)