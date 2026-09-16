def rotate(x, y, degree):
    radian = float(degree) * 2 * math.pi / 360.0
    newx = math.cos(radian) * x - math.sin(radian) * y
    newy = math.sin(radian) * x + math.cos(radian) * y
    return newx, newy