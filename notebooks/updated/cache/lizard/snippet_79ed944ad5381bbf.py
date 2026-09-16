def events(self):
    ret = []
    while True:
        e = self.poll()
        if e is None:
            break
        ret.append(e)
    return ret