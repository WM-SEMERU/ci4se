def mousePress(self, button):
    log.debug('mousePress %s', button)
    buttons = self.buttons | 1 << button - 1
    self.mouseDown(button)
    self.mouseUp(button)
    return self