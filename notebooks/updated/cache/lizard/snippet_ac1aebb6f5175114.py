def setTimeStart(self, timeStart):
    timeStart = QTime(timeStart)
    length = self.length()
    self._timeStart = timeStart
    self._timeEnd = timeStart.addSecs(length * 60)
    self.markForRebuild()