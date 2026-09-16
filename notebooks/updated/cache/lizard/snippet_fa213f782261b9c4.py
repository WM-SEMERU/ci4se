def pluck_each(records, columns):
    return [pluck(records[i], *columns) for i, _ in enumerate(records)]