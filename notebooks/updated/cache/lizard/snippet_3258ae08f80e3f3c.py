def _depression_adjustment(self, elevation):
    if elevation <= 0:
        return 0
    r = 6356900
    a1 = r
    h1 = r + elevation
    theta1 = acos(a1 / h1)
    a2 = r * sin(theta1)
    b2 = r - r * cos(theta1)
    h2 = sqrt(pow(a2, 2) + pow(b2, 2))
    alpha = acos(a2 / h2)
    return degrees(alpha)