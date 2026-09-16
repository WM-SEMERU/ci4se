def _onLeftButtonUp(self, evt):
    x = evt.GetX()
    y = self.figure.bbox.height - evt.GetY()
    evt.Skip()
    if self.HasCapture():
        self.ReleaseMouse()
    FigureCanvasBase.button_release_event(self, x, y, 1, guiEvent=evt)