def update_internal(self, value):
    self.block()
    self.set_widget_value(value)
    self.unblock()