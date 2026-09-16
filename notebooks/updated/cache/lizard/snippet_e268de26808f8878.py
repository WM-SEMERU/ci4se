def set_dwelling_current(self, settings):
    self._dwelling_current_settings['now'].update(settings)
    dwelling_axes_to_update = {axis: amps for axis, amps in self.
        _dwelling_current_settings['now'].items() if self._active_axes.get(
        axis) is False if self.current[axis] != amps}
    if dwelling_axes_to_update:
        self._save_current(dwelling_axes_to_update, axes_active=False)