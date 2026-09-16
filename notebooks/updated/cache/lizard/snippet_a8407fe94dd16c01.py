def p_route_deprecation(self, p):
    if len(p) == 5:
        p[0] = True, p[3], p[4]
    elif p[1]:
        p[0] = True, None, None