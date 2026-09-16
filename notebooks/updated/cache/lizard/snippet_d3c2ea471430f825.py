def locate(x1, y1, x2, y2, x3):
    return y1 - 1.0 * (y1 - y2) * (x1 - x3) / (x1 - x2)