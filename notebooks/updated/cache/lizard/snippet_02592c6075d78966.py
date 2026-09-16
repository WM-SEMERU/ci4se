def display_current(self):
    if self.idx_current in self.scene.items():
        self.scene.removeItem(self.idx_current)
    item = QGraphicsRectItem(0, CURR['pos0'], self.parent.value(
        'window_length'), CURR['pos1'])
    item.setPos(self.parent.value('window_start'), 0)
    item.setPen(QPen(Qt.lightGray))
    item.setBrush(QBrush(Qt.lightGray))
    item.setZValue(-10)
    self.scene.addItem(item)
    self.idx_current = item