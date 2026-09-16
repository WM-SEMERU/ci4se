def _where(self, **kwargs):
    out = self
    for k, v in kwargs.items():
        out = out.where(k, lambda i: i == v)
    return out