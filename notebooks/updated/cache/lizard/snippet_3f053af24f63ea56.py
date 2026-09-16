def area(poly):
    if len(poly) < 3:
        return 0
    total = [0, 0, 0]
    num = len(poly)
    for i in range(num):
        vi1 = poly[i]
        vi2 = poly[(i + 1) % num]
        prod = np.cross(vi1, vi2)
        total[0] += prod[0]
        total[1] += prod[1]
        total[2] += prod[2]
    if total == [0, 0, 0]:
        return 0
    result = np.dot(total, unit_normal(poly[0], poly[1], poly[2]))
    return abs(result / 2)