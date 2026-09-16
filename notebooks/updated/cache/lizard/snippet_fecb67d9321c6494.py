def __add_location(self, type, *args):
    if type == 'directory':
        location = umbra.ui.common.store_last_browsed_path(QFileDialog.
            getExistingDirectory(self, 'Add Directory:', RuntimeGlobals.
            last_browsed_path))
    elif type == 'file':
        location = umbra.ui.common.store_last_browsed_path(QFileDialog.
            getOpenFileName(self, 'Add File:', RuntimeGlobals.
            last_browsed_path, 'All Files (*)'))
    elif type == 'editors':
        location = self.__targets_format.format(self.__default_target)
    elif type == 'include_filter':
        location = self.__filters_in_format.format(self.__default_filter_in)
    elif type == 'exclude_filter':
        location = self.__filters_out_format.format(self.__default_filter_out)
    location and self.Where_lineEdit.setText(', '.join(filter(bool, (
        foundations.strings.to_string(self.Where_lineEdit.text()), location))))