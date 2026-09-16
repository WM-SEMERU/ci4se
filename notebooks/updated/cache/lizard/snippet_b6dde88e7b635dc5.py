def update_label(self):
    current_file = str(self.selectedFiles()[0])
    if not '.' in current_file.split(os.path.sep)[-1]:
        current_file += '.hdf5'
    if os.path.isfile(current_file):
        self.setLabelText(QtGui.QFileDialog.Accept, 'Reload')
    elif os.path.isdir(current_file):
        self.setLabelText(QtGui.QFileDialog.Accept, 'Open')
    else:
        self.setLabelText(QtGui.QFileDialog.Accept, 'Create')