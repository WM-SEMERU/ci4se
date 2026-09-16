def init_layout(self):
    widget = self.widget
    for child_widget in self.child_widgets():
        widget.addSubview(child_widget)