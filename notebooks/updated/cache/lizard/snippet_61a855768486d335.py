def learnObjects(self, objects, reset=True):
    self._setLearningMode()
    for objectName, sensationList in objects.iteritems():
        if len(sensationList) == 0:
            continue
        iterations = 0
        for sensations in sensationList:
            for _ in xrange(self.numLearningPoints):
                for col in xrange(self.numColumns):
                    location, coarseFeature, fineFeature = sensations[col]
                    self.locationInputs[col].addDataToQueue(list(location),
                        0, 0)
                    self.coarseSensors[col].addDataToQueue(list(
                        coarseFeature), 0, 0)
                    self.sensors[col].addDataToQueue(list(fineFeature), 0, 0)
                iterations += 1
        if iterations > 0:
            self.network.run(iterations)
        self.objectRepresentationsL2[objectName] = self.getL2Representations()
        self.objectRepresentationsL5[objectName] = self.getL5Representations()
        if reset:
            self._sendReset()