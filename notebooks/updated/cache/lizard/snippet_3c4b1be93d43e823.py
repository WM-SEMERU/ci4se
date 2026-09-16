def distance(line, point):
    x0, y0, x1, y1 = line
    try:
        p1, p2 = point
    except ValueError:
        p1, p2 = middle(point)
    n1 = ascent(line)
    n2 = -1
    n0 = y0 - n1 * x0
    return abs(n1 * p1 + n2 * p2 + n0) / (n1 ** 2 + n2 ** 2) ** 0.5