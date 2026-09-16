def setIcon(self, icon):
    icon = QIcon(icon)
    if icon.isNull():
        self._icon = None
        self._style = XNodeHotspot.Style.Invisible
    else:
        self._icon = icon
        self._style = XNodeHotspot.Style.Icon