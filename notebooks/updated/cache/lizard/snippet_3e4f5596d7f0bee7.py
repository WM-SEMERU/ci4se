def connect_button(instance, prop, widget):
    widget.clicked.connect(getattr(instance, prop))