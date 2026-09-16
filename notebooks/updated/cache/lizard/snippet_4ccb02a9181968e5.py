def mark_current_profile_as_pending(self):
    index = self.profile_combo.currentIndex()
    item = self.profile_combo.model().item(index)
    item.setForeground(QtGui.QColor('red'))