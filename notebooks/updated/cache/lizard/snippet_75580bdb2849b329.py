def on_KeyPress(self, event):
    if event.GetKeyCode() == wx.WXK_UP:
        self.dist10deg += 0.1
        print('Dist per 10 deg: %.1f' % self.dist10deg)
    elif event.GetKeyCode() == wx.WXK_DOWN:
        self.dist10deg -= 0.1
        if self.dist10deg <= 0:
            self.dist10deg = 0.1
        print('Dist per 10 deg: %.1f' % self.dist10deg)
    elif event.GetKeyCode() == 49:
        widgets = [self.modeText, self.wpText]
        self.toggleWidgets(widgets)
    elif event.GetKeyCode() == 50:
        widgets = [self.batOutRec, self.batInRec, self.voltsText, self.
            ampsText, self.batPerText]
        self.toggleWidgets(widgets)
    elif event.GetKeyCode() == 51:
        widgets = [self.rollText, self.pitchText, self.yawText]
        self.toggleWidgets(widgets)
    elif event.GetKeyCode() == 52:
        widgets = [self.airspeedText, self.altitudeText, self.climbRateText]
        self.toggleWidgets(widgets)
    elif event.GetKeyCode() == 53:
        widgets = [self.altHistRect, self.altPlot, self.altMarker, self.
            altText2]
        self.toggleWidgets(widgets)
    elif event.GetKeyCode() == 54:
        widgets = [self.headingTri, self.headingText, self.headingNorthTri,
            self.headingNorthText, self.headingWPTri, self.headingWPText]
        self.toggleWidgets(widgets)
    self.canvas.draw()
    self.canvas.Refresh()
    self.Refresh()
    self.Update()