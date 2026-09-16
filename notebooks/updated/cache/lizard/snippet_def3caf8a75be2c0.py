def median(values, simple=True, mean_weight=0.0):
    if OR(v == None for v in values):
        Log.error('median is not ready to handle None')
    try:
        if not values:
            return Null
        l = len(values)
        _sorted = sorted(values)
        middle = int(l / 2)
        _median = float(_sorted[middle])
        if len(_sorted) == 1:
            return _median
        if simple:
            if l % 2 == 0:
                return (_sorted[middle - 1] + _median) / 2
            return _median
        start_index = middle - 1
        while start_index > 0 and _sorted[start_index] == _median:
            start_index -= 1
        start_index += 1
        stop_index = middle + 1
        while stop_index < l and _sorted[stop_index] == _median:
            stop_index += 1
        num_middle = stop_index - start_index
        if l % 2 == 0:
            if num_middle == 1:
                return (_sorted[middle - 1] + _median) / 2
            else:
                return _median - 0.5 + (middle - start_index) / num_middle
        elif num_middle == 1:
            return (1 - mean_weight) * _median + mean_weight * (_sorted[
                middle - 1] + _sorted[middle + 1]) / 2
        else:
            return _median - 0.5 + (middle + 0.5 - start_index) / num_middle
    except Exception as e:
        Log.error('problem with median of {{values}}', values=values, cause=e)