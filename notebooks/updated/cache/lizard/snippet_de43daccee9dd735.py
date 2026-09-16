def show_busy(self):
    self.progress_bar.show()
    self.parent.pbnNext.setEnabled(False)
    self.parent.pbnBack.setEnabled(False)
    self.parent.pbnCancel.setEnabled(False)
    self.parent.repaint()
    enable_busy_cursor()
    QgsApplication.processEvents()