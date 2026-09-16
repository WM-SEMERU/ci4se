def InitAgeCheck(self):
    age_df = self.contribution.tables['ages'].df
    self.panel = wx.Panel(self, style=wx.SIMPLE_BORDER)
    self.grid_frame = grid_frame3.GridFrame(self.contribution, self.WD,
        'ages', 'ages', self.panel, main_frame=self.main_frame)
    self.grid_frame.exitButton.SetLabel('Save and continue')
    grid = self.grid_frame.grid
    self.grid_frame.Bind(wx.EVT_BUTTON, lambda event: self.onContinue(event,
        grid, None), self.grid_frame.exitButton)
    self.backButton = wx.Button(self.grid_frame.panel, id=-1, label='Back',
        name='back_btn')
    self.Bind(wx.EVT_BUTTON, lambda event: self.onbackButton(event, self.
        InitLocCheck), self.backButton)
    self.grid_frame.main_btn_vbox.Add(self.backButton, flag=wx.ALL, border=5)
    self.grid_frame.do_fit(None, self.min_size)
    self.grid_frame.Centre()
    return