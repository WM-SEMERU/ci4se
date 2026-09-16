def OnAttributesToolbarToggle(self, event):
    self.main_window.attributes_toolbar.SetGripperVisible(True)
    attributes_toolbar_info = self.main_window._mgr.GetPane(
        'attributes_toolbar')
    self._toggle_pane(attributes_toolbar_info)
    event.Skip()