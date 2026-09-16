def addTab(self, tab):
    if not isinstance(tab, XViewPanelItem):
        tab = XViewPanelItem(tab, self)
        tab.setFixedHeight(self.height())
    index = len(self.items())
    self.layout().insertWidget(index, tab)
    self.setCurrentIndex(index)
    return tab