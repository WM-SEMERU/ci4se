def tags(self):
    return dict([(t, self._catalog.tags.get(t, t)) for t in self._asset.get
        ('tags', [])])