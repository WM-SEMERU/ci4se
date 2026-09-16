def on_install(self, editor):
    self._clear_caches()
    self._update_style()
    super(PygmentsSH, self).on_install(editor)