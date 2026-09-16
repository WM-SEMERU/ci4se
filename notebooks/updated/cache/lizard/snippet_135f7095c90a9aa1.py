def _color_button_clicked(self, n, top):
    self._button_save.setEnabled(True)
    if top:
        self._color_dialogs_top[n].open()
    else:
        self._color_dialogs_bottom[n].open()