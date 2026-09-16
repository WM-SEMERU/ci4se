def findRecordItem(self, record, parent=None):
    try:
        item = self._recordMapping[record]()
    except KeyError:
        return None
    if item is None:
        self._recordMapping.pop(record)
    return item