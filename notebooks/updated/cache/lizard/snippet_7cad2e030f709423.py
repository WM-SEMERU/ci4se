def percentAt(self, value):
    min_val = self.minimum()
    max_val = self.maximum()
    total_seconds = (max_val - min_val).total_seconds()
    value_seconds = (value - min_val).total_seconds()
    if value < min_val:
        return 0.0
    elif max_val < value:
        return 1.0
    try:
        perc = value_seconds / float(total_seconds)
    except ZeroDivisionError:
        perc = 0.0
    return perc