def linkChildFeaturesToParents(self):
    for featureParts in self.byFeatureName.itervalues():
        for feature in featureParts:
            self._linkFeature(feature)