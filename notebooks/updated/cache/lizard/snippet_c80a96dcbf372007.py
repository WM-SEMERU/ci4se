def pythag(a, b):
    absA = abs(a)
    absB = abs(b)
    if absA > absB:
        return absA * sqrt(1.0 + (absB / float(absA)) ** 2)
    elif absB == 0.0:
        return 0.0
    else:
        return absB * sqrt(1.0 + (absA / float(absB)) ** 2)