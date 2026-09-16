def load(self, items):
    for k, vals in items:
        self[k] = ''.join(vals)