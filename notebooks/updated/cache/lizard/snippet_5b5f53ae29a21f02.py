def to_before_pedalboard(self):
    if self.pedalboard is None:
        raise CurrentPedalboardError('The current pedalboard is None')
    before_index = self.pedalboard.index - 1
    if before_index == -1:
        before_index = len(self.bank.pedalboards) - 1
    self.set_pedalboard(self.bank.pedalboards[before_index])