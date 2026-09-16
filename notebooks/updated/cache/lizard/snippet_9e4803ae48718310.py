def on_change_specimen_mouse_cursor(self, event):
    if not self.specimen_EA_xdata or not self.specimen_EA_ydata:
        return
    pos = event.GetPosition()
    width, height = self.canvas2.get_width_height()
    pos[1] = height - pos[1]
    xpick_data, ypick_data = pos
    xdata_org = self.specimen_EA_xdata
    ydata_org = self.specimen_EA_ydata
    data_corrected = self.specimen_eqarea.transData.transform(vstack([
        xdata_org, ydata_org]).T)
    xdata, ydata = data_corrected.T
    xdata = list(map(float, xdata))
    ydata = list(map(float, ydata))
    e = 4.0
    if self.specimen_EA_setting == 'Zoom':
        self.canvas2.SetCursor(wx.Cursor(wx.CURSOR_CROSS))
    else:
        self.canvas2.SetCursor(wx.Cursor(wx.CURSOR_ARROW))
    for i, (x, y) in enumerate(zip(xdata, ydata)):
        if 0 < sqrt((x - xpick_data) ** 2.0 + (y - ypick_data) ** 2.0) < e:
            self.canvas2.SetCursor(wx.Cursor(wx.CURSOR_HAND))
            break
    event.Skip()