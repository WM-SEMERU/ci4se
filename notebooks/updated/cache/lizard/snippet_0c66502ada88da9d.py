def mouseMoveEvent(self, event):
    self.declaration.mouse_move_event(event)
    super(QtGraphicsView, self).mouseMoveEvent(event)