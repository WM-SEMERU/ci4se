def save_visible_toolbars(self):
    toolbars = []
    for toolbar in self.visible_toolbars:
        toolbars.append(toolbar.objectName())
    CONF.set('main', 'last_visible_toolbars', toolbars)