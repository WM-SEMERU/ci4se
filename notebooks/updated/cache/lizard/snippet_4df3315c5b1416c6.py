def pick(self):
    v = random.uniform(0, self.ub)
    d = self.dist
    c = self.vc - 1
    s = self.vc
    while True:
        s = s / 2
        if s == 0:
            break
        if v <= d[c][1]:
            c -= s
        else:
            c += s
            while len(d) <= c:
                s = s / 2
                c -= s
                if s == 0:
                    break
    if c == len(d) or v <= d[c][1]:
        c -= 1
    return d[c][0]