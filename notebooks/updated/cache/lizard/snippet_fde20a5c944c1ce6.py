def copy(self, extra=None):
    if extra is None:
        extra = dict()
    bestModel = self.bestModel.copy(extra)
    avgMetrics = self.avgMetrics
    subModels = self.subModels
    return CrossValidatorModel(bestModel, avgMetrics, subModels)