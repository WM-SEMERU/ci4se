def overlap(ival0, ival1):
    min0, max0 = ival0
    min1, max1 = ival1
    return max(0, min(max0, max1) - max(min0, min1)) > 0