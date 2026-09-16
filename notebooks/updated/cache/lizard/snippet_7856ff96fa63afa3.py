def addRegion(self, name, text, row, column):
    region = XDropZoneRegion(self)
    region.setObjectName(name)
    region.setText(text)
    region.hide()
    self.layout().addWidget(region, row, column)
    return region