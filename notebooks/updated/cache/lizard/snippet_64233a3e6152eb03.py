def addThreeLayers(self, inc, hidc, outc):
    self.addLayer('input', inc)
    self.addContextLayer('context', hidc, 'hidden')
    self.addLayer('hidden', hidc)
    self.addLayer('output', outc)
    self.connect('input', 'hidden')
    self.connect('context', 'hidden')
    self.connect('hidden', 'output')