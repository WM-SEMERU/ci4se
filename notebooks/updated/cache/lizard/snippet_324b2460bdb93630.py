def _onLeftButtonDClick(self, evt):
    x = evt.GetX()
    y = self.figure.bbox.height - evt.GetY()
    evt.Skip()
    self.CaptureMouse()
    FigureCanvasBase.button_press_event(self, x, y, 1, dblclick=True,
        guiEvent=evt)