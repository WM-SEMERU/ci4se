def setPositionLinkedTo(self, widgets):
    if type(widgets) in (list, set, tuple):
        new_widgets = list(widgets)
    else:
        new_widgets = []
        widget = widgets
        while widget:
            widget.installEventFilter(self)
            new_widgets.append(widget)
            widget = widget.parent()
    self._positionLinkedTo = new_widgets