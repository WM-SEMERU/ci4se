def nextPlot(self):
    if self.stacker.currentIndex() < self.stacker.count():
        self.stacker.setCurrentIndex(self.stacker.currentIndex() + 1)