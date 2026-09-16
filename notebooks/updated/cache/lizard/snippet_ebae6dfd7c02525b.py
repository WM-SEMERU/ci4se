def setMaximum(self, value):
    super(XRatingSlider, self).setMaximum(value)
    self.adjustMinimumWidth()