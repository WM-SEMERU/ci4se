def flipVertical(self):
    self.flipV = not self.flipV
    self._transmogrophy(self.angle, self.percent, self.scaleFromCenter,
        self.flipH, self.flipV)