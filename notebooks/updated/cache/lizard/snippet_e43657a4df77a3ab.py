def save_file(self, path=None, force_overwrite=False, just_settings=False,
    **kwargs):
    if not 'binary' in kwargs:
        kwargs['binary'] = self.combo_binary.get_text()
    if just_settings:
        d = _d.databox()
    else:
        d = self
    for x in self._autosettings_controls:
        self._store_gui_setting(d, x)
    _d.databox.save_file(d, path, self.file_type, self.file_type,
        force_overwrite, **kwargs)