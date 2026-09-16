def _create_font_size_combo(self):
    self.std_font_sizes = config['font_default_sizes']
    font_size = str(get_default_font().GetPointSize())
    self.font_size_combo = wx.ComboBox(self, -1, value=font_size, size=(60,
        -1), choices=map(unicode, self.std_font_sizes), style=wx.
        CB_DROPDOWN | wx.TE_PROCESS_ENTER)
    self.font_size_combo.SetToolTipString(_('Text size\n(points)'))
    self.AddControl(self.font_size_combo)
    self.Bind(wx.EVT_COMBOBOX, self.OnTextSize, self.font_size_combo)
    self.Bind(wx.EVT_TEXT_ENTER, self.OnTextSize, self.font_size_combo)