def _addDPFiles(self, *files):
    self.new_entry_dialog.addDataProducts(self.purrer.makeDataProducts([(
        file, True) for file in files], unbanish=True, unignore=True))