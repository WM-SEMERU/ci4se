def load_file(self, path=None, just_settings=False):
    if just_settings:
        d = _d.databox()
        header_only = True
    else:
        d = self
        header_only = False
    if not None == _d.databox.load_file(d, path, filters=self.file_type,
        header_only=header_only, quiet=just_settings):
        for x in self._autosettings_controls:
            self._load_gui_setting(x, d)
    self._synchronize_controls()
    if not just_settings:
        self.plot()
        self.after_load_file()