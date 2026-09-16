def cloneQuery(self, limit=_noItem, sort=_noItem):
    newq = self.query.cloneQuery(limit=limit, sort=sort)
    return self.__class__(newq)