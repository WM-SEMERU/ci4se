def _create_minimum_needs_action(self):
    icon = resources_path('img', 'icons', 'show-minimum-needs.svg')
    self.action_minimum_needs = QAction(QIcon(icon), self.tr(
        'Minimum Needs Calculator'), self.iface.mainWindow())
    self.action_minimum_needs.setStatusTip(self.tr(
        'Open InaSAFE minimum needs calculator'))
    self.action_minimum_needs.setWhatsThis(self.tr(
        'Open InaSAFE minimum needs calculator'))
    self.action_minimum_needs.triggered.connect(self.show_minimum_needs)
    self.add_action(self.action_minimum_needs, add_to_toolbar=self.full_toolbar
        )