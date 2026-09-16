def as_dict(self):
    d = MSONable.as_dict(self)
    d['data'] = self.data.tolist()
    return d