def _triplify_object(self, data, parent):
    subject = self.get_subject(data)
    if self.path:
        yield subject, TYPE_SCHEMA, self.path, TYPE_SCHEMA
    if parent is not None:
        yield parent, self.predicate, subject, TYPE_LINK
        if self.reverse is not None:
            yield subject, self.reverse, parent, TYPE_LINK
    for prop in self.properties:
        for res in prop.triplify(data.get(prop.name), subject):
            yield res