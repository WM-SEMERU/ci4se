def clear_annot(self):
    msgBox = QMessageBox(QMessageBox.Question, 'Clear Annotations',
        'Do you want to remove all the annotations?')
    msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msgBox.setDefaultButton(QMessageBox.Yes)
    response = msgBox.exec_()
    if response == QMessageBox.No:
        return
    self.reset()