def _rescale(vector):
    min_val = min(vector)
    vector = [(v - min_val) for v in vector]
    max_val = float(max(vector))
    try:
        return [(v / max_val) for v in vector]
    except ZeroDivisionError:
        return [1.0] * len(vector)