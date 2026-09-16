def create_widget(self):
    widget = QDoubleSpinBox(self.parent_widget())
    widget.setKeyboardTracking(False)
    self.widget = widget