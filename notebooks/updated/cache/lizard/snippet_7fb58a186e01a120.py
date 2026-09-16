def doUnitConversions(self):
    for det in range(1, self._numchips + 1, 1):
        chip = self._image[self.scienceExt, det]
        conversionFactor = self.effGain
        chip._gain = self.effGain
        chip.effGain = self.effGain
        chip._conversionFactor = conversionFactor