def AddToLayout(self, layout):
    for param in self.params:
        widget = param.RenderWidget()
        layout.addRow(param.caption, widget)