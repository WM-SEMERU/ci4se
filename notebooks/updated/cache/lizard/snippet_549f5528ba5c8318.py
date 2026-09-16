def get_banks(self):
    if self.retrieved:
        raise errors.IllegalState('List has already been retrieved.')
    self.retrieved = True
    return objects.BankList(self._results, runtime=self._runtime)