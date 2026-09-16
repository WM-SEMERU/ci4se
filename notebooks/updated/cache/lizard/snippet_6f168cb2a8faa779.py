def register_view(self, view):
    super(SingleWidgetWindowController, self).register_view(view)
    self.shortcut_manager = ShortcutManager(self.view['main_window'])
    self.register_actions(self.shortcut_manager)
    view['main_window'].connect('destroy', Gtk.main_quit)