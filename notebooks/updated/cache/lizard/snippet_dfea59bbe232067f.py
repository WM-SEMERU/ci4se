def widthratio(value, max_value, max_width):
    ratio = float(value) / float(max_value)
    return int(round(ratio * max_width))