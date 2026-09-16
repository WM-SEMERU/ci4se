def add_vbar_widget(self, ref, x=1, y=1, length=10):
    if ref not in self.widgets:
        widget = widgets.VBarWidget(screen=self, ref=ref, x=x, y=y, length=
            length)
        self.widgets[ref] = widget
        return self.widgets[ref]