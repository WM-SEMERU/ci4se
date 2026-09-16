def add_string_widget(self, ref, text='Text', x=1, y=1):
    if ref not in self.widgets:
        widget = widgets.StringWidget(screen=self, ref=ref, text=text, x=x, y=y
            )
        self.widgets[ref] = widget
        return self.widgets[ref]