def _assign(self, values):
    LOGGER.debug('Assigning values: %r', values)
    if not values:
        return
    keys = self.keys()
    if not self._ref:
        keys.append('_ref')
    if isinstance(values, dict):
        for key in keys:
            if values.get(key):
                if isinstance(values.get(key), list):
                    items = list()
                    for item in values[key]:
                        if isinstance(item, dict):
                            if '_ref' in item:
                                obj_class = get_class(item['_ref'])
                                if obj_class:
                                    items.append(obj_class(self._session,
                                        **item))
                        else:
                            items.append(item)
                    setattr(self, key, items)
                else:
                    setattr(self, key, values[key])
    elif isinstance(values, list):
        self._assign(values[0])
    else:
        LOGGER.critical('Unhandled return type: %r', values)