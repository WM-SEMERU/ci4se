def update_cycles(self):
    self.idx_cycle.clear()
    try:
        self.cycles = self.parent.notes.annot.get_cycles()
    except ValueError as err:
        self.idx_cycle.setEnabled(False)
        msg = 'There is a problem with the cycle markers: ' + str(err)
        self.parent.statusBar().showMessage(msg)
    else:
        if self.cycles is None:
            self.idx_cycle.setEnabled(False)
        else:
            self.idx_cycle.setEnabled(True)
            for i in range(len(self.cycles)):
                self.idx_cycle.addItem(str(i + 1))