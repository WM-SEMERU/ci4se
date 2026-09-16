def openCurrentItem(self):
    logger.debug('openCurrentItem')
    _currentItem, currentIndex = self.getCurrentItem()
    if not currentIndex.isValid():
        return
    self.expand(currentIndex)