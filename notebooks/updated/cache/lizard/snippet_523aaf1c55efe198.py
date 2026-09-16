def mmGetCellActivityPlot(self, title=None, showReset=False, resetShading=0.25
    ):
    cellTrace = self._mmTraces['activeCells'].data
    cellCount = self.getNumColumns()
    activityType = 'Cell Activity'
    return self.mmGetCellTracePlot(cellTrace, cellCount, activityType,
        title=title, showReset=showReset, resetShading=resetShading)