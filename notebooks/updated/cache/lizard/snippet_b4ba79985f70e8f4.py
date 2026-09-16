def centerOnItems(self, items=None):
    if not items:
        rect = self.scene().visibleItemsBoundingRect()
        if not rect.width():
            rect = self.scene().sceneRect()
        self.centerOn(rect.center())
    else:
        self.centerOn(self.scene().calculateBoundingRect(items).center())