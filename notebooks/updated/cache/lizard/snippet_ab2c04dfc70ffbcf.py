def is_shortcut_in_use(self, shortcut):
    for path, actionName, action in foundations.walkers.dictionaries_walker(
        self.__categories):
        if action.shortcut() == QKeySequence(shortcut):
            return True
    return False