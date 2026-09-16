def directory_button_clicked(self):
    self.output_directory.setText(QFileDialog.getExistingDirectory(self,
        self.tr('Select download directory')))