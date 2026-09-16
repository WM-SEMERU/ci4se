def as_widget(self, widget=None, attrs=None, only_initial=False):
    if not widget:
        widget = self.field.widget
    if DJANGO_VERSION > (1, 10):
        widget._field = self.field
        if not isinstance(widget, NgWidgetMixin):
            widget.__class__ = type(widget.__class__.__name__, (
                NgWidgetMixin, widget.__class__), {})
    return super(NgBoundField, self).as_widget(widget, attrs, only_initial)