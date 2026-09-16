def OnInt(self, event):
    value = event.GetValue()
    current_time = time.clock()
    if current_time < self.last_change_s + 0.01:
        return
    self.last_change_s = current_time
    self.cursor_pos = wx.TextCtrl.GetInsertionPoint(self) + 1
    if event.GetValue() > self.no_tabs - 1:
        value = self.no_tabs - 1
    self.switching = True
    post_command_event(self, self.GridActionTableSwitchMsg, newtable=value)
    self.switching = False