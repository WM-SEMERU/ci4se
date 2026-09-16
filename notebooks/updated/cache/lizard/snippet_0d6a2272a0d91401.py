def p_radl(self, t):
    if len(t) == 2:
        t[0] = RADL()
        t[0].add(t[1])
    else:
        t[0] = t[1]
        t[0].add(t[2])