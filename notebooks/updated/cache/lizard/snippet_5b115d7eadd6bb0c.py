def getPointOnLine(x1, y1, x2, y2, n):
    x = (x2 - x1) * n + x1
    y = (y2 - y1) * n + y1
    return x, y