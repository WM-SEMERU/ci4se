def open_file_dialog(self):
    dialog = QtWidgets.QFileDialog
    sender = self.sender()
    if sender == self.btn_open_source:
        textbox = self.source_path
    elif sender == self.btn_open_target:
        textbox = self.target_path
    folder = dialog.getExistingDirectory(self, 'Select a file:', textbox.
        text(), options=QtWidgets.QFileDialog.ShowDirsOnly)
    if str(folder) != '':
        textbox.setText(folder)
        if sender == self.btn_open_source:
            self.reset_avaliable(folder)