def add(self, item):
    if self._is_stringable(item) or self._is_qstring(item):
        self.items.append(PlainText(item))
    elif isinstance(item, MessageElement):
        self.items.append(item)
    elif item is None or hasattr(item, 'isNull') and item.isNull():
        self.items.append(PlainText(tr('Null (None) found from the data.')))
    elif isinstance(item, tuple) or isinstance(item, list):
        for i in item:
            self.add(i)
    else:
        raise InvalidMessageItemError(item, item.__class__)