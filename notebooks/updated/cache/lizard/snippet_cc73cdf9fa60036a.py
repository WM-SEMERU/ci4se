def export_setting(self):
    LOGGER.debug('Export button clicked')
    home_directory = os.path.expanduser('~')
    file_name = self.organisation_line_edit.text().replace(' ', '_')
    file_path, __ = QFileDialog.getSaveFileName(self, self.tr(
        'Export InaSAFE settings'), os.path.join(home_directory, file_name +
        '.json'), self.tr('JSON File (*.json)'))
    if file_path:
        LOGGER.debug('Exporting to %s' % file_path)
        export_setting(file_path)