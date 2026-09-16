def _unsetLearningMode(self):
    for region in self.L4Regions:
        region.setParameter('learn', False)
    for region in self.L2Regions:
        region.setParameter('learningMode', False)