def _last(self, **spec):
    for record in self._entries(spec).order_by(orm.desc(model.Entry.
        local_date), orm.desc(model.Entry.id))[:1]:
        return entry.Entry(record)
    return None