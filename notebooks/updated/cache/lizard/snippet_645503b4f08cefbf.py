def extend(self, other):
    index = len(self)
    length = 0
    for length, element in enumerate(other, 1):
        super(ObservableList, self).append(element)
    if length:
        self._notify_add_at(index, length)