def unhook_drag(self):
    widget = self.widget
    del widget.mousePressEvent
    del widget.mouseMoveEvent
    del widget.mouseReleaseEvent