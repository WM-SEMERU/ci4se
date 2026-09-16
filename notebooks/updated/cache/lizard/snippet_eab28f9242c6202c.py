def index_item(self, item):
    name_property = getattr(self.__class__, 'name_property', None)
    if name_property is None:
        return None
    name = getattr(item, name_property, None)
    if name is None:
        item.add_error('a %s item has been defined without %s, from: %s' %
            (self.inner_class.my_type, name_property, getattr(item,
            'imported_from', 'Unknown importation source!')))
    elif name in self.name_to_item:
        item = self.manage_conflict(item, name)
    self.name_to_item[name] = item
    return item