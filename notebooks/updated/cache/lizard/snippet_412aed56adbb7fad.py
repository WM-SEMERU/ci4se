def to_next_bank(self):
    if self.pedalboard is None:
        raise CurrentPedalboardError('The current pedalboard is None')
    next_index = self.next_bank_index(self.bank.index)
    self.set_bank(self._manager.banks[next_index])