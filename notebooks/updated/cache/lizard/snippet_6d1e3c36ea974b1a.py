def zoomExtents(self):
    rect = self.scene().visibleItemsBoundingRect()
    vrect = self.viewportRect()
    if rect.width():
        changed = False
        scene_rect = self.scene().sceneRect()
        if scene_rect.width() < rect.width():
            scene_rect.setWidth(rect.width() + 150)
            scene_rect.setX(-scene_rect.width() / 2.0)
            changed = True
        if scene_rect.height() < rect.height():
            scene_rect.setHeight(rect.height() + 150)
            scene_rect.setY(-scene_rect.height() / 2.0)
            changed = True
        if changed:
            self.scene().setSceneRect(scene_rect)
        self.fitInView(rect, Qt.KeepAspectRatio)
    if not self.signalsBlocked():
        self.zoomAmountChanged.emit(self.zoomAmount())