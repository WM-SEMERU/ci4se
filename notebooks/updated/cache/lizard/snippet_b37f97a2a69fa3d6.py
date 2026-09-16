def decker_sum(a, b):
    x = a + b
    y = b - (x - a) if abs(a) > abs(b) else a - (x - b)
    return x, y