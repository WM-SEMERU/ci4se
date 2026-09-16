def uncheckButton(self):
    for button in self.buttons:
        button.blockSignals(True)
        if button.isChecked():
            button.setChecked(False)
        button.blockSignals(False)