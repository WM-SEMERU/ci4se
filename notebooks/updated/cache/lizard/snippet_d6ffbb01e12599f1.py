def _create_justification_button(self):
    iconnames = ['JustifyLeft', 'JustifyCenter', 'JustifyRight']
    bmplist = [icons[iconname] for iconname in iconnames]
    self.justify_tb = _widgets.BitmapToggleButton(self, bmplist)
    self.justify_tb.SetToolTipString(_('Justification'))
    self.Bind(wx.EVT_BUTTON, self.OnJustification, self.justify_tb)
    self.AddControl(self.justify_tb)