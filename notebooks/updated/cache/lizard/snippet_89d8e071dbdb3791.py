def view_changed(self):
    if self._resetting:
        return
    if self._viewbox:
        if self._xlim is None:
            args = self._set_range_args or ()
            self.set_range(*args)
        if self._default_state is None:
            self.set_default_state()
        self._update_transform()