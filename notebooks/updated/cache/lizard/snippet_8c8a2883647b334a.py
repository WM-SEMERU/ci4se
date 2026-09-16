def eventFilter(self, object, event):
    if event.type() == event.Resize:
        self.resize(event.size())
    elif event.type() == event.Move:
        self.move(event.pos())
    elif event.type() == event.Close:
        self.setParent(None)
        self.deleteLater()
    return False