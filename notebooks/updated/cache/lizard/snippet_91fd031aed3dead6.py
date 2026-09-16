def set_selected_radio_button(self):
    dont_use_button = self.default_input_button_group.button(len(self.
        _parameter.default_values) - 2)
    dont_use_button.setChecked(True)