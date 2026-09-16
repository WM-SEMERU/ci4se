def create_numeric_stops(breaks, min_value, max_value):
    weight_breaks = scale_between(min_value, max_value, len(breaks))
    return [list(x) for x in zip(breaks, weight_breaks)]