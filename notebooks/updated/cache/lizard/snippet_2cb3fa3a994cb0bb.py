def set_shortcut(self, name, shortcut):
    name = self.__normalize_name(name)
    action = self.get_action(name)
    if not action:
        return
    action.setShortcut(QKeySequence(shortcut))
    return True