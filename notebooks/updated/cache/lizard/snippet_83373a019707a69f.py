def filterAcceptsRow(self, source_row, source_parent):
    model = self.sourceModel()
    item = model.items[source_row]
    key = getattr(item, 'filter', None)
    if key is not None:
        regex = self.filterRegExp()
        if regex.pattern():
            match = regex.indexIn(key)
            return False if match == -1 else True
    for role, values in self.includes.items():
        data = getattr(item, role, None)
        if data not in values:
            return False
    for role, values in self.excludes.items():
        data = getattr(item, role, None)
        if data in values:
            return False
    return super(ProxyModel, self).filterAcceptsRow(source_row, source_parent)