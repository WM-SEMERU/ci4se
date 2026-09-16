def radio_buttons_clicked(self):
    for spin_box in list(self.spin_boxes.values()):
        spin_box.setEnabled(False)
    self.list_widget.setEnabled(False)
    radio_button_checked_id = self.input_button_group.checkedId()
    if radio_button_checked_id > -1:
        selected_value = list(self._parameter.options.values())[
            radio_button_checked_id]
        if selected_value.get('type') == MULTIPLE_DYNAMIC:
            self.list_widget.setEnabled(True)
        elif selected_value.get('type') == SINGLE_DYNAMIC:
            selected_key = list(self._parameter.options.keys())[
                radio_button_checked_id]
            self.spin_boxes[selected_key].setEnabled(True)