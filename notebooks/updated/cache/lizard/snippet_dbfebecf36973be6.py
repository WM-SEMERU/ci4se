def finalize(self):
    self._comboboxListView.removeEventFilter(self)
    self.comboBox.model().rowsInserted.disconnect(self.comboBoxRowsInserted)
    self.comboBox.activated.disconnect(self.comboBoxActivated)
    super(ChoiceCtiEditor, self).finalize()