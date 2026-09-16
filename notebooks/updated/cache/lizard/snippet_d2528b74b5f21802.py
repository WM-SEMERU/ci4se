def handleImplicitCheck(self):
    for button, widget in zip(self.radioButtons, self.widgets):
        if isinstance(widget, CheckBox):
            if button.GetValue():
                widget.setValue(True)
            else:
                widget.setValue(False)