def mousePressEvent(self, event):
    self.setValue(self.valueAt(event.pos().x()))