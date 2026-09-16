def Rectangle(p1=(0, 0, 0), p2=(2, 1, 0), c='k', bc='dg', lw=1, alpha=1,
    texture=None):
    p1 = np.array(p1)
    p2 = np.array(p2)
    pos = (p1 + p2) / 2
    length = abs(p2[0] - p1[0])
    height = abs(p2[1] - p1[1])
    return Plane(pos, [0, 0, -1], length, height, c, bc, alpha, texture)