def save(self, instance):
    cond = tinydb.where('original') == instance.original
    eid = self.update(instance, cond)
    if eid is None:
        return self.create(instance)
    return eid