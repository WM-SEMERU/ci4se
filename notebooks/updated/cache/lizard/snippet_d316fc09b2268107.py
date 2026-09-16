def groups_shelf(self):
    if self._groups_shelf is None:
        self._groups_shelf = shelve.open(self.group_shelf_fqfn, writeback=False
            )
    return self._groups_shelf