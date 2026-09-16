def property(self, name):
    found = None
    if is_uuid(name):
        found = find(self.properties, lambda p: name == p.id)
    else:
        found = find(self.properties, lambda p: name == p.name)
    if not found:
        raise NotFoundError('Could not find property with name or id {}'.
            format(name))
    return found