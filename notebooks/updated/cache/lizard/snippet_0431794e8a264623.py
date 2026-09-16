def _set_properties(self):
    self.codetext_ctrl.SetToolTipString(_('Enter python code here.'))
    self.apply_button.SetToolTipString(_('Apply changes to current macro'))
    self.splitter.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
    self.result_ctrl.SetMinSize((10, 10))