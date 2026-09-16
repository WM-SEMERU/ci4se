def insert(self, index, item):
    super(ObservableList, self).insert(index, item)
    length = len(self)
    if index >= length:
        index = length - 1
    elif index < 0:
        index += length - 1
        if index < 0:
            index = 0
    self._notify_add_at(index)