def history_size_changed(self, settings, key, user_data):
    lines = settings.get_int(key)
    for i in self.guake.notebook_manager.iter_terminals():
        i.set_scrollback_lines(lines)