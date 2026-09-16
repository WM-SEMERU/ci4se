def repr(self, changed_widgets=None):
    if changed_widgets is None:
        changed_widgets = {}
    return super(Widget, self).repr(changed_widgets)