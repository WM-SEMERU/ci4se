def customData(self, key, default=None):
    key = nativestring(key)
    menu = self
    while not key in menu._customData and isinstance(menu.parent(), XMenu):
        menu = menu.parent()
    return menu._customData.get(nativestring(key), default)