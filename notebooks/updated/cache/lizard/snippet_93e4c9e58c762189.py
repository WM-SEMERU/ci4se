def backspace_changed(self, settings, key, user_data):
    for i in self.guake.notebook_manager.iter_terminals():
        i.set_backspace_binding(self.getEraseBinding(settings.get_string(key)))