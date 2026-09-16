def capture(rect=None, filepath='', prompt=True, hideWindow=None):
    widget = XSnapshotWidget(QApplication.desktop())
    widget.setRegion(rect)
    widget.setHideWindow(hideWindow)
    widget.setFilepath(filepath)
    widget.move(1, 1)
    widget.resize(QApplication.desktop().size())
    if prompt or not filepath:
        widget.show()
    else:
        widget.save()