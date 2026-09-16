def _setCurrentRecord(self, item, record):
    try:
        is_record = item.record() == record
    except:
        is_record = False
    if is_record:
        self.setCurrentItem(item)
        return True
    for c in range(item.childCount()):
        if self._setCurrentRecord(item.child(c), record):
            return True
    return False