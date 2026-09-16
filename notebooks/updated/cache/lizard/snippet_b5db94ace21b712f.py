def draw(self):
    if not self.visible:
        return
    if self.isEnabled:
        if (self.mouseIsDown and self.lastMouseDownOverButton and self.
            mouseOverButton):
            if self.value:
                self.window.blit(self.surfaceOnDown, self.loc)
            else:
                self.window.blit(self.surfaceOffDown, self.loc)
        elif self.value:
            self.window.blit(self.surfaceOn, self.loc)
        else:
            self.window.blit(self.surfaceOff, self.loc)
    elif self.value:
        self.window.blit(self.surfaceOnDisabled, self.loc)
    else:
        self.window.blit(self.surfaceOffDisabled, self.loc)