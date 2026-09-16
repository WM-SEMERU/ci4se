def update_result_ctrl(self, event):
    if not self:
        return
    printLen = 0
    self.result_ctrl.SetValue('')
    if hasattr(event, 'msg'):
        self.result_ctrl.AppendText(event.msg)
        printLen = len(event.msg)
    if hasattr(event, 'err'):
        errLen = len(event.err)
        errStyle = wx.TextAttr(wx.RED)
        self.result_ctrl.AppendText(event.err)
        self.result_ctrl.SetStyle(printLen, printLen + errLen, errStyle)
    if not hasattr(event, 'err') or event.err == '':
        if self._ok_pressed:
            self.Destroy()
    self._ok_pressed = False