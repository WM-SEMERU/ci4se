def get(self, ns, label=None):
    query = Tag.query.filter(Tag.ns == ns)
    if label is not None:
        return query.filter(Tag.label == label).first()
    return query.all()