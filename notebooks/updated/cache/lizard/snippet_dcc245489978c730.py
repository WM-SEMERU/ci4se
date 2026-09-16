def initialize(self, useRandomEncoder):
    self.setRandomSeed(self.seed)
    self.dim = numpy.shape(self.spatialConfig)[-1]
    self.spatialMap = dict(zip(map(tuple, list(self.spatialConfig)), self.
        sensoryInputElements))
    self.lengthMotorInput1D = (2 * self.maxDisplacement + 1
        ) * self.numActiveBitsMotorInput
    uniqueSensoryElements = list(set(self.sensoryInputElementsPool))
    if useRandomEncoder:
        self.sensoryEncoder = SDRCategoryEncoder(n=1024, w=self.
            numActiveBitsSensoryInput, categoryList=uniqueSensoryElements,
            forced=True)
        self.lengthSensoryInput = self.sensoryEncoder.getWidth()
    else:
        self.lengthSensoryInput = (len(self.sensoryInputElementsPool) + 1
            ) * self.numActiveBitsSensoryInput
        self.sensoryEncoder = CategoryEncoder(w=self.
            numActiveBitsSensoryInput, categoryList=uniqueSensoryElements,
            forced=True)
    motorEncoder1D = ScalarEncoder(n=self.lengthMotorInput1D, w=self.
        numActiveBitsMotorInput, minval=-self.maxDisplacement, maxval=self.
        maxDisplacement, clipInput=True, forced=True)
    self.motorEncoder = VectorEncoder(length=self.dim, encoder=motorEncoder1D)