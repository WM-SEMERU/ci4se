def isValidUnit(self, w):
    bad = set(['point', 'a'])
    if w in bad:
        return False
    try:
        pq.Quantity(0.0, w)
        return True
    except:
        return w == '/'