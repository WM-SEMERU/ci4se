def setChecked(self, tocheck):
    layout = self.layout()
    for i in range(layout.count()):
        w = layout.itemAt(i).widget()
        if w.text() in tocheck:
            w.setChecked(True)