def goForward(self):
    if self._slideshow.currentIndex() == self._slideshow.count() - 1:
        self.finished.emit()
    else:
        self._slideshow.slideInNext()