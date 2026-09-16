def resizeToContents(self):
    if self.count():
        item = self.item(self.count() - 1)
        rect = self.visualItemRect(item)
        height = rect.bottom() + 8
        height = max(28, height)
        self.setFixedHeight(height)
    else:
        self.setFixedHeight(self.minimumHeight())