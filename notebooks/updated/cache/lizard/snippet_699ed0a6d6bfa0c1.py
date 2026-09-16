def add(self, item):
    if isinstance(item, list):
        self.rows.append(Row(item))
    elif isinstance(item, Row):
        self.rows.append(item)
    else:
        raise InvalidMessageItemError(item, item.__class__)