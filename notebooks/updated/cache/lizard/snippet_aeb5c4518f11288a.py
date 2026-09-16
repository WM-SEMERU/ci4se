def iter_conditions(condition):
    conditions = list()
    visited = set()
    if condition.operation in {'and', 'or'}:
        conditions.extend(reversed(condition.values))
    elif condition.operation == 'not':
        conditions.append(condition.values[0])
    else:
        conditions.append(condition)
    while conditions:
        condition = conditions.pop()
        if condition in visited:
            continue
        visited.add(condition)
        yield condition
        if condition.operation in {'and', 'or', 'not'}:
            conditions.extend(reversed(condition.values))