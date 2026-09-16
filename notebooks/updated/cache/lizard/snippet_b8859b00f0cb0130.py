def on_paint(self, event):
    dc = wx.AutoBufferedPaintDC(self)
    dc.DrawBitmap(self._bmp, 0, 0)