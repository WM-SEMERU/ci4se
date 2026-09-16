def normalize(self, dt):
    if dt.tzinfo is None:
        raise ValueError('Naive time - no tzinfo set')
    offset = dt.tzinfo._utcoffset
    dt = dt.replace(tzinfo=None)
    dt = dt - offset
    return self.fromutc(dt)