def restore_state(self):
    settings = QtCore.QSettings()
    flag = bool(settings.value('inasafe/useDefaultTemplates', True, type=bool))
    self.default_template_radio.setChecked(flag)
    try:
        default_template_path = resources_path('qgis-composer-templates',
            'inasafe-map-report-portrait.qpt')
        path = settings.value('inasafe/lastTemplate', default_template_path,
            type=str)
        self.template_combo.setCurrentIndex(self.template_combo.findData(path))
    except TypeError:
        self.template_combo.setCurrentIndex(2)
    try:
        path = settings.value('inasafe/lastCustomTemplate', '', type=str)
    except TypeError:
        path = ''
    self.template_path.setText(path)