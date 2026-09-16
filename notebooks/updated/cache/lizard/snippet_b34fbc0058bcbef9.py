def addChanged(self):
    if self.addWidget.currentIndex() == 0:
        return
    typ = asUnicode(self.addWidget.currentText())
    self.param.addNew(typ)
    self.addWidget.setCurrentIndex(0)