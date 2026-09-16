def _sense(self, featureSDR, learn, waitForSettle):
    for monitor in self.monitors.values():
        monitor.beforeSense(featureSDR)
    iteration = 0
    prevCellActivity = None
    while True:
        inputParams, locationParams = self.column.sensoryCompute(featureSDR,
            learn)
        if waitForSettle:
            cellActivity = set(self.column.getSensoryRepresentation()), set(
                self.column.getLocationRepresentation())
            if cellActivity == prevCellActivity:
                break
            prevCellActivity = cellActivity
        for monitor in self.monitors.values():
            if iteration > 0:
                monitor.beforeSensoryRepetition()
            monitor.afterInputCompute(**inputParams)
            monitor.afterLocationAnchor(**locationParams)
        iteration += 1
        if not waitForSettle or iteration >= self.maxSettlingTime:
            break