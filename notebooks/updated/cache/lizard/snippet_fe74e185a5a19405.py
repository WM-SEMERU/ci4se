def _create_multi_buffer_action(self):
    icon = resources_path('img', 'icons', 'show-multi-buffer.svg')
    self.action_multi_buffer = QAction(QIcon(icon), self.tr('Multi Buffer'),
        self.iface.mainWindow())
    self.action_multi_buffer.setStatusTip(self.tr('Open InaSAFE multi buffer'))
    self.action_multi_buffer.setWhatsThis(self.tr('Open InaSAFE multi buffer'))
    self.action_multi_buffer.triggered.connect(self.show_multi_buffer)
    self.add_action(self.action_multi_buffer, add_to_toolbar=self.full_toolbar)