def _binning(values, limits=(0, 0), bin_num=10):
    if limits == (0, 0):
        eps = 1.0 / sys.maxint
        min_val, max_val = min(values) - eps, max(values) + eps
    else:
        min_val, max_val = limits
    bin_size = (max_val - min_val) / float(bin_num)
    bins = [0] * bin_num
    out_points = 0
    for value in values:
        try:
            if value - min_val < 0:
                out_points += 1
            else:
                index = int((value - min_val) / float(bin_size))
                bins[index] += 1
        except IndexError:
            out_points += 1
    result = []
    center = bin_size / 2 + min_val
    for i, y in enumerate(bins):
        x = center + bin_size * i
        result.append((x, y))
    return result