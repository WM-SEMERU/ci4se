def new_profile(self):
    dir = os.path.join(QgsApplication.qgisSettingsDirPath(), 'inasafe',
        'minimum_needs')
    file_name, __ = QFileDialog.getSaveFileName(self, self.tr(
        'Create a minimum needs profile'), expanduser(dir), self.tr(
        'JSON files (*.json *.JSON)'), options=QFileDialog.DontUseNativeDialog)
    if not file_name:
        return
    file_name = basename(file_name)
    if self.profile_combo.findText(file_name) == -1:
        minimum_needs = {'resources': [], 'provenance': '', 'profile':
            file_name}
        self.minimum_needs.update_minimum_needs(minimum_needs)
        self.minimum_needs.save_profile(file_name)
        self.profile_combo.addItem(file_name)
        self.clear_resource_list()
        self.profile_combo.setCurrentIndex(self.profile_combo.findText(
            file_name))
    else:
        self.profile_combo.setCurrentIndex(self.profile_combo.findText(
            file_name))
        self.select_profile_by_name(file_name)