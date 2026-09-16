def write_headers(self):
    hlist = []
    for h in self.headers:
        hlist.append('{}: {}'.format(h.key, h.value))
    return hlist