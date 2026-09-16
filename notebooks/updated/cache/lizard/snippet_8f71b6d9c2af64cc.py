def fill_datetime(self):
    if not self.filled:
        raise SlotNotFilledError(
            'Slot with name "%s", key "%s" not yet filled.' % (self.name,
            self.key))
    return self._fill_datetime