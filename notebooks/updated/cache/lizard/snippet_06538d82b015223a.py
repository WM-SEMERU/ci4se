def _update_fontcolor(self, fontcolor):
    textcolor = wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOWTEXT)
    textcolor.SetRGB(fontcolor)
    self.textcolor_choice.SetColour(textcolor)