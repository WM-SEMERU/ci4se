def find_item_by_id(self, object_id):
    if isinstance(object_id, Item):
        return object_id
    if not isinstance(object_id, string_types):
        logger.debug('Find an item by id, object_id is not int nor string: %s',
            object_id)
        return object_id
    for items in [self.hosts, self.services, self.actions, self.checks,
        self.hostgroups, self.servicegroups, self.contacts, self.contactgroups
        ]:
        if object_id in items:
            return items[object_id]
    logger.error('Item with id %s not found', str(object_id))
    return None