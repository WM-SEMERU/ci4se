def on_btn_metadata(self, event):
    if not self.check_for_meas_file():
        return
    if not self.check_for_uncombined_files():
        return
    if self.data_model_num == 2:
        wait = wx.BusyInfo('Compiling required data, please wait...')
        wx.SafeYield()
        self.ErMagic_frame = ErMagicBuilder.MagIC_model_builder(self.WD,
            self, self.er_magic)
    elif self.data_model_num == 3:
        wait = wx.BusyInfo('Compiling required data, please wait...')
        wx.SafeYield()
        self.ErMagic_frame = ErMagicBuilder.MagIC_model_builder3(self.WD,
            self, self.contribution)
    self.ErMagic_frame.Show()
    self.ErMagic_frame.Center()
    size = wx.DisplaySize()
    size = size[0] - 0.3 * size[0], size[1] - 0.3 * size[1]
    self.ErMagic_frame.Raise()
    del wait