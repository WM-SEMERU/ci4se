def set_corner_widgets(self, corner_widgets):
    assert isinstance(corner_widgets, dict)
    assert all(key in (Qt.TopLeftCorner, Qt.TopRightCorner) for key in
        corner_widgets)
    self.corner_widgets.update(corner_widgets)
    for corner, widgets in list(self.corner_widgets.items()):
        cwidget = QWidget()
        cwidget.hide()
        prev_widget = self.cornerWidget(corner)
        if prev_widget:
            prev_widget.close()
        self.setCornerWidget(cwidget, corner)
        clayout = QHBoxLayout()
        clayout.setContentsMargins(0, 0, 0, 0)
        for widget in widgets:
            if isinstance(widget, int):
                clayout.addSpacing(widget)
            else:
                clayout.addWidget(widget)
        cwidget.setLayout(clayout)
        cwidget.show()