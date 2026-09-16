def dist(self, *args, **kwargs):
    out = self._orb.dist(*args, **kwargs)
    if len(out) == 1:
        return out[0]
    else:
        return out