def save_shortcuts(self):
    self.check_shortcuts()
    for shortcut in self.source_model.shortcuts:
        shortcut.save()