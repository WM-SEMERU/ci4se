def enable_radio_button(self):
    for button in self.default_input_button_group.buttons():
        button.setEnabled(True)
    self.set_selected_radio_button()
    self.custom_value.setEnabled(True)