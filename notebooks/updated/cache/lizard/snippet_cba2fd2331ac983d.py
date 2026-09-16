def boost(self, **kw):
    new = self._clone()
    new.field_boosts.update(kw)
    return new