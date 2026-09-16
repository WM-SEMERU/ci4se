def recalculate(self):
    scene = self.scene()
    w = self.calculateSceneWidth()
    scene.setSceneRect(0, 0, w, self.height())
    spacing = self.spacing()
    x = self.width() / 4.0
    y = self.height() / 2.0
    for item in self.items():
        pmap = item.pixmap()
        item.setPos(x, y - pmap.height() / 1.5)
        x += pmap.size().width() + spacing