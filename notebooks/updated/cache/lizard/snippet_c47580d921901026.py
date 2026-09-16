def cycle_dist(x, y, n):
    dist = abs(x - y) % n
    if dist >= 0.5 * n:
        dist = n - dist
    return dist