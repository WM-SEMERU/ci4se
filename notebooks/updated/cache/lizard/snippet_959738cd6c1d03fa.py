def onSave(self, grid):
    if self.drop_down_menu:
        self.drop_down_menu.clean_up()
    self.grid_builder.save_grid_data()
    wx.MessageBox('Saved!', 'Info', style=wx.OK | wx.ICON_INFORMATION)