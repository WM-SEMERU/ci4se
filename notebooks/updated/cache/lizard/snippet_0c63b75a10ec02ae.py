def addRecord(self, record):
    label_mapper = self.labelMapper()
    icon_mapper = self.iconMapper()
    self.addItem(label_mapper(record))
    self.setItemData(self.count() - 1, wrapVariant(record), Qt.UserRole)
    if icon_mapper:
        self.setItemIcon(self.count() - 1, icon_mapper(record))
    if self.showTreePopup():
        XOrbRecordItem(self.treePopupWidget(), record)