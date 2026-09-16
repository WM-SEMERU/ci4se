def create_shortcuts(self, parent):
    findnext = config_shortcut(self.find_next, context='_', name=
        'Find next', parent=parent)
    findprev = config_shortcut(self.find_previous, context='_', name=
        'Find previous', parent=parent)
    togglefind = config_shortcut(self.show, context='_', name='Find text',
        parent=parent)
    togglereplace = config_shortcut(self.show_replace, context='_', name=
        'Replace text', parent=parent)
    hide = config_shortcut(self.hide, context='_', name=
        'hide find and replace', parent=self)
    return [findnext, findprev, togglefind, togglereplace, hide]