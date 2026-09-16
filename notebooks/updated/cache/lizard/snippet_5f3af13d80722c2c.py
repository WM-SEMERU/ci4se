def __check_focus(self, event):
    changed = False
    if not self._curfocus:
        changed = True
    elif self._curfocus != self.focus():
        self.__clear_inplace_widgets()
        changed = True
    newfocus = self.focus()
    if changed:
        if newfocus:
            self._curfocus = newfocus
            self.__focus(newfocus)
        self.__updateWnds()