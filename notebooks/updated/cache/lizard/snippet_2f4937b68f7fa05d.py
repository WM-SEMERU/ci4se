def on_change_dir_button(self, event=None):
    currentDirectory = self.WD
    change_dir_dialog = wx.DirDialog(self.panel,
        'Choose your working directory to create or edit a MagIC contribution:'
        , defaultPath=currentDirectory, style=wx.DD_DEFAULT_STYLE | wx.
        DD_NEW_DIR_BUTTON | wx.DD_CHANGE_DIR)
    result = change_dir_dialog.ShowModal()
    if result == wx.ID_CANCEL:
        return
    if result == wx.ID_OK:
        self.WD = change_dir_dialog.GetPath()
        self.dir_path.SetValue(self.WD)
    change_dir_dialog.Destroy()
    self.get_wd_data()