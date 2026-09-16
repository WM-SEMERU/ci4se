def create_ui(self):
    super(GtkShapesCanvasView, self).create_ui()
    self.widget.set_events(gtk.gdk.BUTTON_PRESS | gtk.gdk.BUTTON_RELEASE |
        gtk.gdk.BUTTON_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.
        BUTTON_RELEASE_MASK | gtk.gdk.POINTER_MOTION_HINT_MASK)
    self._dirty_check_timeout_id = gtk.timeout_add(30, self.check_dirty)
    self.resize = Debounce(self._resize, wait=250)
    debounced_on_expose_event = Debounce(self._on_expose_event, wait=250,
        leading=True, trailing=True)
    self.widget.connect('expose-event', debounced_on_expose_event)