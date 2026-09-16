def changed(self, item):
    if self._rejectChanges:
        raise errors.ChangeRejected()
    if self.transaction is not None:
        self.transaction.add(item)
        self.touched.add(item)