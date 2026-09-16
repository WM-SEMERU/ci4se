def unzoom_all(self, event=None, panel=None):
    if panel is None:
        panel = self.current_panel
    self.panels[panel].unzoom_all(event=event)