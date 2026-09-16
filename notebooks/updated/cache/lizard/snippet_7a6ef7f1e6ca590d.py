def start(widget, processEvents=True, style=None, movie=None):
    if style is None:
        style = os.environ.get('PROJEXUI_LOADER_STYLE', 'gray')
    parent = widget.parent()
    while isinstance(parent, QSplitter):
        parent = parent.parent()
    loader = getattr(widget, '_private_xloader_widget', None)
    if not loader:
        loader = XLoaderWidget(parent, style)
        widget.destroyed.connect(loader.deleteLater)
        setattr(widget, '_private_xloader_widget', loader)
        setattr(widget, '_private_xloader_count', 0)
        loader.move(widget.pos())
        if widget.isVisible():
            loader.show()
        if movie:
            loader.setMovie(movie)
        widget.installEventFilter(loader)
    else:
        count = getattr(widget, '_private_xloader_count', 0)
        setattr(widget, '_private_xloader_count', count + 1)
    loader.resize(widget.size())
    return loader