def onEdit(self):
    with transactUI(self):
        if self.buildSpec['poll_external_updates']:
            self.fetchExternalUpdates()
        self.showSettings()