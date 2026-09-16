def _get_ancestors_path(self, model, levels=None):
    if not issubclass(model, self.model):
        raise ValueError('%r is not a subclass of %r' % (model, self.model))
    ancestry = []
    parent_link = model._meta.get_ancestor_link(self.model)
    if levels:
        levels -= 1
    while parent_link is not None:
        related = parent_link.remote_field
        ancestry.insert(0, related.get_accessor_name())
        if levels or levels is None:
            parent_model = related.model
            parent_link = parent_model._meta.get_ancestor_link(self.model)
        else:
            parent_link = None
    return LOOKUP_SEP.join(ancestry)