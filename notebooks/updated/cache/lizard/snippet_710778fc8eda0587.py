def _save_settings(self):
    if self._autosettings_path == None:
        return
    gui_settings_dir = _os.path.join(_cwd, 'egg_settings')
    if not _os.path.exists(gui_settings_dir):
        _os.mkdir(gui_settings_dir)
    path = _os.path.join(gui_settings_dir, self._autosettings_path)
    settings = _g.QtCore.QSettings(path, _g.QtCore.QSettings.IniFormat)
    settings.clear()
    if hasattr_safe(self._window, 'saveState'):
        settings.setValue('State', self._window.saveState())
    settings.setValue('Geometry', self._window.saveGeometry())