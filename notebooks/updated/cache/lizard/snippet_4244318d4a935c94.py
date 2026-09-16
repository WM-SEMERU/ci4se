def make_palette(self):
    p = array('B')
    t = array('B')
    for x in self.palette:
        p.extend(x[0:3])
        if len(x) > 3:
            t.append(x[3])
    p = tostring(p)
    t = tostring(t)
    if t:
        return p, t
    return p, None