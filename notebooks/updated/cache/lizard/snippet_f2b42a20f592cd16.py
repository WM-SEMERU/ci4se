def handleEvent(self, eventObj):
    if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN
        ) or not self._visible:
        return []
    retVal = []
    hasExited = False
    if not self.mouseOverButton and self._rect.collidepoint(eventObj.pos):
        self.mouseOverButton = True
        self.mouseEnter(eventObj)
        retVal.append('enter')
    elif self.mouseOverButton and not self._rect.collidepoint(eventObj.pos):
        self.mouseOverButton = False
        hasExited = True
    if self._rect.collidepoint(eventObj.pos):
        if eventObj.type == MOUSEMOTION:
            self.mouseMove(eventObj)
            retVal.append('move')
        elif eventObj.type == MOUSEBUTTONDOWN:
            self.buttonDown = True
            self.lastMouseDownOverButton = True
            self.mouseDown(eventObj)
            retVal.append('down')
    elif eventObj.type in (MOUSEBUTTONUP, MOUSEBUTTONDOWN):
        self.lastMouseDownOverButton = False
    doMouseClick = False
    if eventObj.type == MOUSEBUTTONUP:
        if self.lastMouseDownOverButton:
            doMouseClick = True
        self.lastMouseDownOverButton = False
        if self.buttonDown:
            self.buttonDown = False
            self.mouseUp(eventObj)
            retVal.append('up')
        if doMouseClick:
            self.buttonDown = False
            self.mouseClick(eventObj)
            retVal.append('click')
    if hasExited:
        self.mouseExit(eventObj)
        retVal.append('exit')
    return retVal