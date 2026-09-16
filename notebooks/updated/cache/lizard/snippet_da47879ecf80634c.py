def init_widget(self):
    super(AndroidPicker, self).init_widget()
    d = self.declaration
    w = self.widget
    if d.items:
        self.set_items(d.items)
    else:
        if d.max_value:
            self.set_max_value(d.max_value)
        if d.min_value:
            self.set_min_value(d.min_value)
    self.set_value(d.value)
    if d.wraps:
        self.set_wraps(d.wraps)
    if d.long_press_update_interval:
        self.set_long_press_update_interval(d.long_press_update_interval)
    w.setOnValueChangedListener(w.getId())
    w.onValueChange.connect(self.on_value_change)