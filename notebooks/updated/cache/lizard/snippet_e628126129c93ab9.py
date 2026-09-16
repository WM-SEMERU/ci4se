def _event_ignored(self, event):
    if event.canvas.widgetlock.locked():
        return True
    if event.artist not in self.artists:
        return True
    if not self.hover:
        if event.mouseevent.button != self.display_button:
            return True
    return False