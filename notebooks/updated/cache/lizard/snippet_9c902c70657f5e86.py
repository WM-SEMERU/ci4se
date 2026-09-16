def set_single_click_to_open(self, value):
    self.single_click_to_open = value
    self.parent_widget.sig_option_changed.emit('single_click_to_open', value)