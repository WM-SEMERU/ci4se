def add_widget(self, widget):
    self._widgets.append(widget)
    widget.parent = self
    self._update_child_widgets()
    return widget