def layout(self):
    ret = []
    for row in self.rows:
        if len(row) > len(ret):
            ret += [0] * (len(row) - len(ret))
        for n, field in enumerate(row):
            if field is self.empty_value:
                field = ''
            ret[n] = max(ret[n], len(field))
    return ret