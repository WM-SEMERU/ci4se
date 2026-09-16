def learnObjects(self):
    for objectName, objectFeatures in self.objects.iteritems():
        self.reset()
        for module in self.locationModules:
            module.activateRandomLocation()
        for feature in objectFeatures:
            locationOnObject = feature['top'] + feature['height'] / 2, feature[
                'left'] + feature['width'] / 2
            self.move(objectName, locationOnObject)
            featureName = feature['name']
            featureSDR = self.features[featureName]
            for _ in xrange(10):
                self.sense(featureSDR, learn=True)
            self.locationRepresentations[objectName, locationOnObject
                ] = self.getActiveLocationCells()
            self.inputRepresentations[objectName, locationOnObject, featureName
                ] = self.inputLayer.getActiveCells()
        self.objectRepresentations[objectName
            ] = self.objectLayer.getActiveCells()