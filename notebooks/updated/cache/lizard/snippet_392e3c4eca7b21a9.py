def _dihed_cos_low(a, b, c, deriv):
    a = Vector3(9, deriv, a, (0, 1, 2))
    b = Vector3(9, deriv, b, (3, 4, 5))
    c = Vector3(9, deriv, c, (6, 7, 8))
    b /= b.norm()
    tmp = b.copy()
    tmp *= dot(a, b)
    a -= tmp
    tmp = b.copy()
    tmp *= dot(c, b)
    c -= tmp
    a /= a.norm()
    c /= c.norm()
    return dot(a, c).results()