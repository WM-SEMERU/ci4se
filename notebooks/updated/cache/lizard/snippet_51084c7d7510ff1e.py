def _do_layout(self):
    label_style = wx.LEFT | wx.ALIGN_CENTER_VERTICAL
    button_style = (wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.
        ALIGN_CENTER_VERTICAL | wx.FIXED_MINSIZE)
    grid_sizer_1 = wx.GridSizer(4, 2, 3, 3)
    grid_sizer_1.Add(self.Rows_Label, 0, label_style, 3)
    grid_sizer_1.Add(self.X_DimensionsEntry, 0, wx.EXPAND, 0)
    grid_sizer_1.Add(self.Columns_Label, 0, label_style, 3)
    grid_sizer_1.Add(self.Y_DimensionsEntry, 0, wx.EXPAND, 0)
    grid_sizer_1.Add(self.Tabs_Label, 0, label_style, 3)
    grid_sizer_1.Add(self.Z_DimensionsEntry, 0, wx.EXPAND, 0)
    grid_sizer_1.Add(self.ok_button, 0, button_style, 3)
    grid_sizer_1.Add(self.cancel_button, 0, button_style, 3)
    self.SetSizer(grid_sizer_1)
    grid_sizer_1.Fit(self)
    self.Layout()
    self.X_DimensionsEntry.SetFocus()