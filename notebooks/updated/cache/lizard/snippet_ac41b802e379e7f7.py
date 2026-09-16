def status(self, s=None):
    if s is None:
        return self.states[self._status]
    if isinstance(s, str):
        s = self.states.index(s)
    self._status = s
    self.textproperty.SetLineOffset(self.offset)
    self.actor.SetInput(self.spacer + self.states[s] + self.spacer)
    s = s % len(self.colors)
    self.textproperty.SetColor(colors.getColor(self.colors[s]))
    bcc = numpy.array(colors.getColor(self.bcolors[s]))
    self.textproperty.SetBackgroundColor(bcc)
    if self.showframe:
        self.textproperty.FrameOn()
        self.textproperty.SetFrameWidth(self.framewidth)
        self.textproperty.SetFrameColor(numpy.sqrt(bcc))